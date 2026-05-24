# GitHub Pages Setup

## 1. Publish Source

This repository includes a GitHub Actions workflow:

```text
.github/workflows/pages.yml
```

After you push it to GitHub, the `Actions` tab will show `Deploy GitHub Pages`. If the workflow file has not been pushed yet, the `Actions` tab can look empty.

The workflow includes:

```yaml
with:
  enablement: true
```

This lets `actions/configure-pages` create/enable the Pages site when GitHub has not created it yet. Without this, the deploy can fail with:

```text
Get Pages site failed. Please verify that the repository has Pages enabled...
```

In GitHub:

1. Open repository `Settings`.
2. Go to `Pages`.
3. Set `Build and deployment` to `GitHub Actions`.
4. Save.

If the workflow still fails, manually save this setting once, then rerun `Deploy GitHub Pages` from the `Actions` tab.

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
