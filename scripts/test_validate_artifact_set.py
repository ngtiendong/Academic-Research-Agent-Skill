#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_artifact_set.py")
SPEC = importlib.util.spec_from_file_location("validate_artifact_set", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ArtifactValidatorTests(unittest.TestCase):
    def test_project_profile_and_links_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "01_Paper1_Pipeline_State.md").write_text(
                "[scope](02_Paper1_Scope.md)\n", encoding="utf-8"
            )
            (root / "02_Paper1_Scope.md").write_text("# Scope\n", encoding="utf-8")
            (root / "20_Paper1_Reality_Gate.md").write_text(
                "**Verdict:** `BLOCK`\n", encoding="utf-8"
            )
            (root / "23_Paper1_Feasibility_Pilot_Protocol.md").write_text(
                "**Status:** `NOT AUTHORIZED`\n", encoding="utf-8"
            )
            errors, artifacts = VALIDATOR.validate_names(root)
            errors += VALIDATOR.validate_links(root)
            errors += VALIDATOR.validate_gate(root, artifacts, True)
            self.assertEqual([], errors)

    def test_reserved_slot_repurpose_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "03_Paper1_Hypothesis_Decision_Map.md").write_text(
                "# Wrong slot\n", encoding="utf-8"
            )
            errors, _ = VALIDATOR.validate_names(root)
            self.assertTrue(any("slot 03" in error for error in errors))

    def test_link_inside_code_fence_is_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "00_Index.md").write_text(
                "```md\n[example](missing.md)\n```\n", encoding="utf-8"
            )
            self.assertEqual([], VALIDATOR.validate_links(root))

    def test_block_rejects_deep_plan_and_unlabeled_pilot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "20_Reality_Gate.md").write_text("Verdict: BLOCK\n", encoding="utf-8")
            (root / "12_Code_Execution_Plan.md").write_text("# Plan\n", encoding="utf-8")
            (root / "23_Feasibility_Pilot_Protocol.md").write_text(
                "# Pilot\n", encoding="utf-8"
            )
            _, artifacts = VALIDATOR.validate_names(root)
            errors = VALIDATOR.validate_gate(root, artifacts, True)
            self.assertEqual(2, len(errors))


if __name__ == "__main__":
    unittest.main()
