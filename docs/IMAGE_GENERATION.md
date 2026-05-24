# Image Generation Guide

The repository already includes:

- Hero image: `docs/assets/research-agent-hero.png`
- Social preview: `docs/assets/social-preview.png`
- Image prompts: `assets/image-prompts/README.md`
- Mermaid diagram source files: `docs/visuals/`

## Recommended Images

| Asset | Target path | Size |
|---|---|---|
| Hero image | `docs/assets/research-agent-hero.png` | 16:9 wide |
| Social preview | `docs/assets/social-preview.png` | 1280x640 |
| README workflow screenshot | `docs/assets/workflow-preview.png` | 16:9 |
| Human-agent collaboration visual | `docs/assets/collaboration-preview.png` | 16:9 |

## How to Generate More Images

1. Open `assets/image-prompts/README.md`.
2. Copy the prompt you want.
3. Use your image generation tool.
4. Save the result into `docs/assets/`.
5. Reference it from `README.md` or `docs/index.html`.

Example Markdown:

```md
![Human-agent research collaboration](docs/assets/collaboration-preview.png)
```

Example HTML:

```html
<img src="assets/collaboration-preview.png" alt="Human-agent research collaboration" />
```

## Style Rules

Use visuals that show:

- student-centered research,
- human decision gates,
- literature and evidence artifacts,
- technical fields such as CS, AI, math, and engineering,
- agent support around the human researcher.

Avoid visuals that imply:

- the AI writes the paper alone,
- fake acceptance or fake results,
- a robot replacing the researcher,
- generic dark hacker aesthetics,
- unreadable UI text.

## Prompt Template

```text
Create a polished GitHub README illustration for "Research Agent Skill", a human-guided AI research agent for Master and PhD students in computer science, AI, mathematics, and engineering. Show a student researcher at the center making decisions, surrounded by transparent AI agent panels for literature grounding, novelty gate, math formalization, experiment planning, reviewer simulation, and claim verification. Modern academic workspace, scientific, trustworthy, clean, high clarity, no logos, no readable small text, no robot replacing the student, 16:9.
```

## Social Preview

For GitHub social preview, use:

```text
docs/assets/social-preview.png
```

Then set it in:

```text
GitHub repository -> Settings -> Social preview
```
