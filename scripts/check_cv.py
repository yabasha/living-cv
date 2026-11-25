"""Check the CV's repository-relative links and required sections."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^ )]+)\)")
HTML_LINK = re.compile(r'\b(?:src|href)="([^"]+)"')
HEADING = re.compile(r"^#{1,6} (.+)$", re.MULTILINE)
FENCE = re.compile(r"^ {0,3}(?:\x60{3,}|~{3,}).*$", re.MULTILINE)
REQUIRED = {
    "README.md": [
        "# Bashar Ayyash | AI Systems Architect & Tech Lead",
        "I build production AI systems for regulated industries",
        "[Experience](experience/README.md)",
        "[Case studies](case-studies/README.md)",
        "[How I work](how-i-work.md)",
        "[Releases](https://github.com/yabasha/living-cv/releases)",
    ],
    "experience/README.md": ["# Experience"],
    "case-studies/README.md": ["# Case studies"],
    "CHANGELOG.md": ["# Changelog", "## [Unreleased]"],
    ".github/pull_request_template.md": ["## Review checklist"],
    ".github/ISSUE_TEMPLATE/cv-correction.md": ["## Public evidence"],
}


def heading_ids(path):
    slugs = set()
    for heading in HEADING.findall(path.read_text(encoding="utf-8")):
        base = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        slug = base
        duplicate = 0
        while slug in slugs:
            duplicate += 1
            slug = f"{base}-{duplicate}"
        slugs.add(slug)
    return slugs


def link_problem(path, link):
    target = urlsplit(link)
    if target.scheme or target.netloc:
        if target.scheme == "https" and target.hostname:
            return None
        if target.scheme == "mailto" and "@" in target.path:
            return None
        return "expected a valid HTTPS or email link"

    destination = (path.parent / unquote(target.path)).resolve() if target.path else path
    if not destination.is_relative_to(ROOT):
        return "destination is outside the repository"
    if not destination.is_file():
        return "destination file is missing"
    if target.fragment and destination.suffix == ".md":
        if unquote(target.fragment) not in heading_ids(destination):
            return "destination heading is missing"
    return None


def main():
    errors = []
    for filename, expected in REQUIRED.items():
        path = ROOT / filename
        if not path.is_file():
            errors.append(f"{filename}: required file is missing")
            continue
        content = path.read_text(encoding="utf-8")
        for element in expected:
            if element not in content:
                errors.append(f"{filename}: missing {element}")

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        content = path.read_text(encoding="utf-8")
        for section in FENCE.split(content)[::2]:
            for link in LINK.findall(section) + HTML_LINK.findall(section):
                problem = link_problem(path, link)
                if problem:
                    errors.append(f"{path.relative_to(ROOT)}: {problem} ({link})")

    if errors:
        print("\n".join(errors))
        return 1
    print("CV structure and repository-relative links passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
