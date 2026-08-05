#!/usr/bin/env python3
"""Validate research artifact naming, relative links, and coarse gate consistency."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


SLOT_RULES: dict[str, tuple[str, re.Pattern[str]]] = {
    "01": ("state", re.compile(r"^(?:Project_State|Pipeline_State)$")),
    "02": ("scope", re.compile(r"^Scope$")),
    "03": ("draft", re.compile(r"^Draft(?:_.+)?$")),
    "04": ("literature_review", re.compile(r"^Literature_Review(?:_.+)?$")),
    "05": ("literature_grounding", re.compile(r"^(?:Lit_Grounding|Literature_Grounding)(?:_.+)?$")),
    "06": ("math_formalization", re.compile(r"^(?:Math|Mathematical)_Formalization(?:_.+)?$")),
    "07": ("reviewer_simulation", re.compile(r"^ReviewerSim(?:_.+)?$")),
    "08": ("review_fixes", re.compile(r"^ReviewFixes(?:_.+)?$")),
    "15": ("changelog", re.compile(r"^Changelog(?:_.+)?$")),
    "18": ("source_notes_index", re.compile(r"^(?:Source|Paper)_Notes_Index(?:_.+)?$")),
    "19": ("source_analysis_matrix", re.compile(r"^(?:Source|Paper)_Analysis_Matrix(?:_.+)?$")),
    "20": ("reality_gate", re.compile(r"^Reality_Gate$")),
    "21": ("hypothesis_decision_map", re.compile(r"^Hypothesis_Decision_Map$")),
    "22": ("experimental_unit_audit", re.compile(r"^Experimental_Unit_Audit_Plan$")),
    "23": ("feasibility_pilot", re.compile(r"^Feasibility_Pilot_Protocol$")),
    "24": ("mechanism_method_routing", re.compile(r"^Mechanism_Method_Routing$")),
}

FILE_RE = re.compile(r"^(?P<slot>\d{2})_(?P<body>.+)\.md$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
FENCE_RE = re.compile(r"(?:```|~~~).*?(?:```|~~~)", re.DOTALL)
VERDICT_RE = re.compile(
    r"(?:Verdict|Reality(?:/execution)?(?: verdict)?)[^\n`]*`?"
    r"(BLOCK|FEASIBILITY_PILOT_ONLY|EXECUTION_READY|FULL_RUN_READY)`?",
    re.IGNORECASE,
)
DEEP_PLAN_RE = re.compile(
    r"(?:Draft|Execution_Risk_Plan|Risk_Plan|WorkBreakdown|Code_Execution_Plan|"
    r"Implementation_Guide|Agent_Brief)",
    re.IGNORECASE,
)


def logical_body(body: str) -> str:
    """Remove only the supported project identifier prefix."""
    return re.sub(r"^Paper\d+_", "", body)


def markdown_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1 : value.index(">")]
    else:
        value = value.split(maxsplit=1)[0]
    return unquote(value.split("#", 1)[0])


def validate_names(root: Path) -> tuple[list[str], dict[str, list[Path]]]:
    errors: list[str] = []
    by_artifact: dict[str, list[Path]] = defaultdict(list)

    for path in sorted(root.glob("*.md")):
        match = FILE_RE.match(path.name)
        if not match:
            errors.append(f"non-canonical Markdown filename: {path.name}")
            continue
        slot = match.group("slot")
        rule = SLOT_RULES.get(slot)
        if rule is None:
            continue
        artifact, pattern = rule
        body = logical_body(match.group("body"))
        if not pattern.fullmatch(body):
            errors.append(
                f"slot {slot} is reserved for {artifact}, not {match.group('body')}: {path.name}"
            )
            continue
        by_artifact[artifact].append(path)

    for artifact, paths in sorted(by_artifact.items()):
        if len(paths) > 1:
            names = ", ".join(path.name for path in paths)
            errors.append(f"duplicate logical artifact {artifact}: {names}")
    return errors, by_artifact


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    for source in sorted(root.rglob("*.md")):
        text = FENCE_RE.sub("", source.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            raw = match.group("target")
            if raw.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = markdown_target(raw)
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                display = source.relative_to(root)
                errors.append(f"broken relative link in {display}: {raw}")
    return errors


def validate_gate(
    root: Path, by_artifact: dict[str, list[Path]], strict_gates: bool
) -> list[str]:
    if not strict_gates or not by_artifact.get("reality_gate"):
        return []

    errors: list[str] = []
    gate_path = by_artifact["reality_gate"][0]
    gate_text = gate_path.read_text(encoding="utf-8")
    match = VERDICT_RE.search(gate_text)
    if not match:
        return [f"cannot find a canonical Reality Gate verdict in {gate_path.name}"]

    verdict = match.group(1).upper()
    if verdict not in {"BLOCK", "FEASIBILITY_PILOT_ONLY"}:
        return errors

    for path in sorted(root.glob("*.md")):
        if path == gate_path:
            continue
        if DEEP_PLAN_RE.search(path.stem):
            errors.append(f"{verdict} is inconsistent with downstream artifact: {path.name}")

    for path in by_artifact.get("feasibility_pilot", []):
        status_text = path.read_text(encoding="utf-8")[:1500].upper()
        if verdict == "BLOCK" and "NOT AUTHORIZED" not in status_text:
            errors.append(
                f"BLOCK requires the feasibility protocol to be explicitly NOT AUTHORIZED: {path.name}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="artifact folder to validate")
    parser.add_argument(
        "--strict-gates",
        action="store_true",
        help="also check coarse consistency between the Reality Gate and downstream artifacts",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR: artifact folder does not exist: {root}", file=sys.stderr)
        return 2

    name_errors, by_artifact = validate_names(root)
    errors = name_errors + validate_links(root) + validate_gate(root, by_artifact, args.strict_gates)
    if errors:
        print(f"Artifact validation failed ({len(errors)} error(s)):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Artifact validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
