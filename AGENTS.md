# AGENTS.md

This repository is Bashar Ayyash’s public living CV. Keep changes readable for recruiters and safe for public Git history.

## Where to make changes

- [README.md](README.md) is the recruiter landing page. Keep it concise and link to details.
- [Experience](experience/README.md) is the employer index. Put role details and accomplishments on each employer’s own page.
- [Case studies](case-studies/README.md) hold longer project write-ups. Update the index when adding or moving a case study.
- Record recruiter-visible changes under `[Unreleased]` in the [changelog](CHANGELOG.md).

## Writing and privacy

- Use plain, first-person language in the CV. Verify dates, titles, responsibilities, and metrics. Cite public sources for claims when available. Generalize or omit unverified and confidential details.
- Keep private application material, referee names and contact details, private file locations, credentials, and proprietary material out of commits, issues, PRs, releases, and CI logs.
- Use [Bashar’s contact page](https://yabasha.dev/contact) or `hello@yabasha.dev` for professional inquiries. The [references policy](experience/references.md) allows sharing reference details for a specific role only after an offer and Bashar’s explicit approval.
- Keep the public CV in Markdown. Use GitHub’s noreply address for commit author and committer metadata.

## Verifying a change

- Run `python3 scripts/check_cv.py` from the repository root. It checks required sections and repository-relative links. GitHub Actions runs the same command on PRs and pushes to `main`.
- Follow changed external links and preview affected Markdown on GitHub. Check that the experience and case-study links still work from the landing page.
- Review the diff and metadata before publishing. For PRs, use the [review checklist](.github/pull_request_template.md).
