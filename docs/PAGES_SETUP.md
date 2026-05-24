# GitHub Pages Setup

## 1. Publish Source

This site is static HTML/CSS, so the most reliable setup is GitHub Pages native branch deployment. Do not use a custom GitHub Actions Pages workflow unless you specifically need a build step.

In GitHub:

1. Open repository `Settings`.
2. Go to `Pages`.
3. Set `Build and deployment` to `Deploy from a branch`.
4. Select branch `main`.
5. Select folder `/docs`.
6. Save.

GitHub will create its own Pages deployment automatically. You may see an internal `pages-build-deployment` run in the `Actions` tab after saving.

If you previously added a custom workflow such as `.github/workflows/pages.yml`, remove it before using branch deployment. Otherwise GitHub may keep trying the failing workflow.

The site will be available at:

```text
https://ngtiendong.github.io/Academic-Research-Agent-Skill/
```

## 2. URLs

This repository is configured for:

```text
https://github.com/ngtiendong/Academic-Research-Agent-Skill
https://ngtiendong.github.io/Academic-Research-Agent-Skill/
```

## 3. Google Indexing

For fastest indexing:

1. Add a custom domain if possible.
2. Verify the domain in Google Search Console.
3. Submit `sitemap.xml`.
4. Request indexing for the homepage.
5. Share the page from LinkedIn, X, Reddit, personal website, lab website, and related awesome lists.

## 4. Social Preview

Use `docs/assets/social-preview.png` as the GitHub social preview image. It is prepared at 1280x640.
