# nbfinance public information

This repository contains only the static information site for a private software prototype. It contains **no finance-application source, financial data, account credentials or bank callback endpoint**.

The owner authorized this separate public repository and GitHub Pages site, and agreed in principle to public information pages for the private pilot. The finance application and its source repository remain private. Only approved explanatory text belongs here: do not copy application source, private checklists, verification logs, financial snapshots, banking exports or configuration into this repository.

## Draft status

The overview, privacy notice and usage notice are **review drafts, not yet adopted**. They now describe the finite private two-account balance pilot, separately from website hosting and contact email. They do not claim that real access has happened, publish application code/data, or offer a banking service to the public.

The owner explicitly approved **Bernhard Slatinsek** as the public operator name and `security@nbsystems.dev` as the public privacy/security contact. No additional identity/contact information is invented. Contact monitoring and the proposed correspondence/rights procedures still require owner confirmation. Purpose-specific applicability/roles, any required hosting/mail processing terms and transfer safeguards, and any additional identity/site disclosures remain adoption checks, not findings that a provider or all private email is unlawful. No account-specific safeguards or legal-compliance certification are claimed.

The November candidates are local preparations: agreement in principle to information pages is not approval of every sentence or a verified deployment. The explicit live-registration prohibition remains until the actual adoption/publication checks are resolved. Do not submit these drafts as completed application policies, register/activate an application or access bank data as part of this website task.

Use an approved GitHub handle/noreply identity for public commits; do not expose a private name/email through commit metadata. Do not publish banking information in issues, pull requests or comments.

## Static deployment

GitHub Pages publishes the `main` branch root with `.nojekyll`. The content is plain HTML and CSS: no JavaScript, forms, cookies set by site code, external fonts, analytics, embeds or banking flow. Contact links open the visitor's email client for the explicitly approved address only.

Expected page paths after deployment are the site root, `privacy.html` and `terms.html`. Actual HTTPS availability must be verified before claiming a live deployment. Do not use the information site as an OAuth redirect/callback or place any authorisation code in its query string.

GitHub Pages logs visitors' IP addresses for security according to its own documentation. The privacy draft links to that documentation and GitHub's Privacy Statement rather than claiming that hosting collects nothing, that the operator performs GitHub's logging, or that the project controls its retention.

## Checks

```sh
python -m unittest discover -s tests -v
```

Local verification evidence, screenshots and credentials are excluded by `.gitignore`. Public pushes must use an explicit file allowlist, a secret scan and a separate private-identifier check: a secret scanner alone does not detect every disclosure. Concrete private identifiers must not appear in public test denylists. The original pages had missing-page RED/GREEN checks; the November update observed content RED on the old pages, then GREEN. Further static checks cover local navigation, HTML metadata and absence of collection/remote asset mechanisms.

## Primary references

- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- https://docs.github.com/en/rest/pages/pages?apiVersion=2022-11-28

These references describe GitHub's infrastructure; they are not a legal compliance certification for the private application.
