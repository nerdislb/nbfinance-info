# nbfinance public information

This repository contains only the static information site for a private software prototype. It contains **no finance-application source, financial data, account credentials or bank callback endpoint**.

The owner authorized this separate public repository and GitHub Pages site. The finance application's source repository remains private. Do not copy content from that private repository, local verification logs, financial snapshots, banking exports or configuration into this repository.

## Draft status

The overview, privacy notice and usage notice are deliberately marked **draft / preparation only**. The owner explicitly approved **Bernhard Slatinsek** as the public operator name for this private household project and `security@nbsystems.dev` as the public privacy/security contact. No postal address, telephone number, additional contact or credentials are published. The remaining application-processing description still requires finalisation. These pages are not a final policy/terms package for live bank-data processing or completed Enable Banking registration; publishing the contact does not create or verify the mailbox.

Use an approved GitHub handle/noreply identity for public commits; do not expose a private name/email through commit metadata. Do not publish banking information in issues, pull requests or comments.

## Static deployment

GitHub Pages publishes the `main` branch root with `.nojekyll`. The content is plain HTML and CSS: no JavaScript, forms, cookies set by site code, external fonts, analytics, embeds or banking flow. Contact links open the visitor's email client for the explicitly approved address only.

Expected page paths after deployment are the site root, `privacy.html` and `terms.html`. Actual HTTPS availability must be verified before claiming a live deployment. Do not use the information site as an OAuth redirect/callback or place any authorisation code in its query string.

GitHub Pages logs visitors' IP addresses for security according to its own documentation. The privacy draft links to that documentation and GitHub's Privacy Statement rather than claiming that hosting collects nothing or promising a retention period controlled by this project.

## Checks

```sh
python -m unittest discover -s tests -v
```

Local verification evidence, screenshots and credentials are excluded by `.gitignore`. Public pushes must use an explicit file allowlist and a secret scan. The three pages have observed missing-page RED then GREEN checks. Further static checks cover local navigation, HTML metadata and absence of collection/remote asset mechanisms.

## Primary references

- https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- https://docs.github.com/en/rest/pages/pages?apiVersion=2022-11-28

These references describe GitHub's infrastructure; they are not a legal compliance certification for the private application.
