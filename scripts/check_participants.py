"""Validate public practice records with the Python standard library."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
USERNAME = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?")


def validate(path: Path) -> list[str]:
    if path.is_symlink() or not path.is_file() or path.suffix != ".md":
        return ["Use a regular Markdown file directly inside participants/."]
    if not USERNAME.fullmatch(path.stem) or "--" in path.stem:
        return ["Name the file after your GitHub username, e.g. octocat.md."]
    if path.stat().st_size > 65536:
        return ["Keep your record under 64 KiB."]
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["Save the file as UTF-8."]
    errors = []
    if not re.search(r"^#\s+\S", content, re.MULTILINE):
        errors.append("Add a Markdown title beginning with '# '.")
    account = re.search(r"^- GitHub:\s*@([A-Za-z0-9-]+)\s*$", content, re.MULTILINE)
    if not account or account[1].lower() != path.stem.lower():
        errors.append("Set '- GitHub: @your-username' to match the filename.")
    if "YOUR_USERNAME" in content or "在这里" in content:
        errors.append("Replace all template placeholders with your own content.")
    sections = re.split(r"^##\s+[^\n]+\n", content, flags=re.MULTILINE)
    if len(sections) < 4 or any(not section.strip() for section in sections[1:]):
        errors.append("Include and fill all three sections from the template.")
    return errors


def main() -> int:
    directory = ROOT / "participants"
    if not directory.is_dir():
        print("Missing participants/ directory.")
        return 1
    failed = False
    paths = sorted(directory.iterdir())
    for path in paths:
        for error in validate(path):
            print(f"{path.relative_to(ROOT)}: {error}")
            failed = True
    if not failed:
        print(f"Validated {len(paths)} participant record(s).")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
