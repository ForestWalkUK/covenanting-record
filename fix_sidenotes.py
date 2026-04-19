"""
fix_sidenotes.py
================
Fixes sidenote placement in Jekyll Markdown files for The Covenanting Record.

PROBLEM:
    Sidenote tags placed after a blank line cause the superscript number to
    appear on its own line below the paragraph rather than inline within it.

FIX:
    Moves <label>, <input>, and <span class="sidenote"> tags inside the
    preceding paragraph, with no blank line separating them, and collapses
    the three tags onto a single unbroken line.

USAGE:
    1. Place this script in the root of your covenanting-record folder, i.e.:
       C:\\Users\\carlh\\Documents\\PubWeb\\Covenanting-Record\\covenanting-record\\

    2. Open a terminal (PowerShell or Command Prompt) in that folder and run:
       python fix_sidenotes.py

    3. The script will process all .md files in _posts/ and _documents/
       and print a summary of changes made.

    4. Review the changes in VS Code or GitHub Desktop before pushing.

SAFETY:
    - Original files are backed up to a _sidenote_backups/ folder before
      any changes are made.
    - Run from the repo root only.
    - Dry-run mode available: set DRY_RUN = True below to preview changes
      without writing anything.
"""

import os
import re
import shutil
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

DRY_RUN = False  # Set to True to preview changes without writing files

FOLDERS = ["_posts", "_documents"]

BACKUP_DIR = "_sidenote_backups"

# ── Regex pattern ─────────────────────────────────────────────────────────────
#
# Matches a block like:
#
#   (optional blank line)
#   <label for="..." class="margin-toggle sidenote-number"></label>
#   <input type="checkbox" id="..." class="margin-toggle"/>
#   <span class="sidenote">...</span>
#
# The span content may span multiple lines.

SIDENOTE_PATTERN = re.compile(
    r'(\n{1,2})'                                        # 1-2 newlines before label
    r'(<label\s+for="([^"]+)"\s+class="margin-toggle'  # <label ...>
    r'(?:\s+sidenote-number)?"\s*></label>)'
    r'\s*\n\s*'                                         # whitespace/newline between tags
    r'(<input\s+type="checkbox"\s+id="[^"]+"\s+'        # <input .../>
    r'class="margin-toggle"\s*/>)'
    r'\s*\n\s*'                                         # whitespace/newline between tags
    r'(<span\s+class="(?:sidenote|marginnote)">'        # <span ...>
    r'(.*?)'                                            # span content (non-greedy)
    r'</span>)',                                        # </span>
    re.DOTALL
)


def fix_sidenotes_in_text(text):
    """
    Finds all sidenote blocks that are separated from the preceding paragraph
    by a blank line, and joins them inline with no preceding blank line.
    Returns (fixed_text, number_of_fixes_made).
    """
    fixes = 0

    def replacer(match):
        nonlocal fixes
        newlines_before = match.group(1)

        # Only fix if there was a blank line (i.e. two newlines) before the label
        if newlines_before == '\n\n':
            fixes += 1
            label   = match.group(2)
            input_  = match.group(4)
            span    = match.group(5)
            # Collapse span content whitespace
            span_clean = re.sub(r'\s+', ' ', span)
            return f'\n{label}<{input_[1:] if input_.startswith("<") else input_}{span_clean}'
        else:
            return match.group(0)  # Already correct, leave untouched

    fixed = SIDENOTE_PATTERN.sub(replacer, text)
    return fixed, fixes


def backup_file(src_path, backup_root):
    """Copies file to backup directory, preserving subfolder structure."""
    rel = src_path.resolve().relative_to(Path.cwd().resolve())
    dest = backup_root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dest)


def process_folder(folder, backup_root, dry_run):
    folder_path = Path(folder)
    if not folder_path.exists():
        print(f"  [SKIP] Folder not found: {folder}")
        return 0, 0

    md_files = list(folder_path.glob("*.md"))
    if not md_files:
        print(f"  [SKIP] No .md files found in {folder}")
        return 0, 0

    total_files_changed = 0
    total_fixes = 0

    for md_file in sorted(md_files):
        original = md_file.read_text(encoding="utf-8")
        fixed, fixes = fix_sidenotes_in_text(original)

        if fixes > 0:
            total_fixes += fixes
            total_files_changed += 1
            if dry_run:
                print(f"  [DRY RUN] Would fix {fixes} sidenote(s) in: {md_file}")
            else:
                backup_file(md_file, backup_root)
                md_file.write_text(fixed, encoding="utf-8")
                print(f"  [FIXED]   {fixes} sidenote(s) corrected in: {md_file}")
        else:
            print(f"  [OK]      No fixes needed in: {md_file}")

    return total_files_changed, total_fixes


def main():
    print("=" * 60)
    print("  Covenanting Record — Sidenote Placement Fixer")
    print("=" * 60)

    if DRY_RUN:
        print("  MODE: DRY RUN (no files will be changed)\n")
    else:
        print("  MODE: LIVE (files will be updated)\n")

    backup_root = Path(BACKUP_DIR)
    grand_total_files = 0
    grand_total_fixes = 0

    for folder in FOLDERS:
        print(f"Processing: {folder}/")
        files_changed, fixes = process_folder(folder, backup_root, DRY_RUN)
        grand_total_files += files_changed
        grand_total_fixes += fixes
        print()

    print("=" * 60)
    if DRY_RUN:
        print(f"  DRY RUN complete.")
        print(f"  Would fix {grand_total_fixes} sidenote(s) across "
              f"{grand_total_files} file(s).")
        print(f"  Set DRY_RUN = False and re-run to apply changes.")
    else:
        print(f"  Done. {grand_total_fixes} sidenote(s) fixed across "
              f"{grand_total_files} file(s).")
        if grand_total_fixes > 0:
            print(f"  Backups saved to: {BACKUP_DIR}/")
        print(f"  Review changes in VS Code or GitHub Desktop before pushing.")
    print("=" * 60)


if __name__ == "__main__":
    main()
