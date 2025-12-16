---
---
description: "Create a new release (@jwadow)"
---

Create release notes for a new version.

## Step 1: Analyze commits (3 commands)

**1.1. Get the latest tag (previous release):**
```bash
git describe --tags --abbrev=0
```

**1.2. Get ALL changes with a single command (full line-by-line diffs of all commits):**
```bash
git log [PREV_TAG]..HEAD -p --reverse
```
This command will show for each commit: message + full line-by-line diff of all files.
Flag `-p` = patch (full diff), `--reverse` = chronological order.

**1.3. Read the affected files in full:**
Use `read_file` to read the current state of all modified files.
This will provide full context for understanding the changes.

## Step 2: Create the release notes file
Create a file `_notes/RELEASE_NOTES_v[VERSION].md` with the following structure:

```markdown
# v[VERSION] - [Catchy Name] Release

---

[Brief one-sentence description of the release]

<!-- STRICTLY AVAILABLE SECTIONS (include only if there are corresponding changes): -->

## 💥 Breaking Changes
[Breaking changes requiring user action]

## ✨ New Features
[New features with descriptions strictly for users, not describing internal code workings]

## 🐛 Bug Fixes
[Bug fixes]

## 🔒 Security
[Security fixes]

## ⚡ Improvements
[Improvements]

## 📝 Documentation
[Documentation changes]

## 🗑️ Deprecated
[Deprecated features that will be removed in the future]

## ❌ Removed
[Removed features]

## ⚙️ Configuration
[Configuration changes - table with variables]

## 📦 Dependencies
[New dependencies]

## 🔄 Upgrade
[If something needs to be updated, for example due to new dependencies, etc. It's important to provide a brief guide on how to properly perform all actions. Ideal template below:]
After downloading and extracting the new release, install dependencies from the project folder:
```bash
pip install -r requirements.txt
```

---

**Full Changelog**: https://github.com/[OWNER]/[REPO]/compare/[PREV_VERSION]...[VERSION]

---

# Git Commands

```bash
git tag -a v[VERSION] -m "[Brief description of the main feature]"
git push origin v[VERSION]
```
```

**File structure:**
- `# v[VERSION] - [Name] Release` — header, used as Title on GitHub Release
- Everything between `---` and `# Git Commands` — copied to the Description field on GitHub
- `# Git Commands` — commands for the user, NOT for agent execution

## Step 3: Check versions in code
Verify that the version is updated in all project files:
1. Find all version mentions: `grep -r "1.0." --include="*.py" --include="*.md"`
2. Ensure `APP_VERSION` in `config.py` matches the release, if present
3. Check `__version__` in `__init__.py`, if present
4. Check other places in case of other programming languages
5. Notify the user if the version is not updated somewhere

## Step 4: Release name
Come up with a name in the format: `v[VERSION] - [Catchy Name] Release`
Examples:
- v1.0.2 - Compatibility Release
- v1.0.3 - Usage Tracking Release

## ⚠️ CRITICALLY IMPORTANT:
1. **DO NOT EXECUTE git tag, git push, or any write git commands!** Only read commands (log, show, diff)
2. **DO NOT INVENT NEW SECTIONS**
3. **THIS IS ALL A RELEASE DESCRIPTION FOR USERS**, so don't include unnecessary things like describing tests and such, as that's for developers
4. Write all git commands for creating tags ONLY in the release notes file
5. Title for GitHub Release = first line `# v[VERSION] - [Name] Release`
6. Description for GitHub Release = everything from the brief description to `# Git Commands`
7. The Upgrade section should be at the bottom, before Full Changelog
8. If there are new pip dependencies, be sure to mention `pip install -r requirements.txt`
9. Create the file in English, but communicate with the user in their language.
10. Ask the user for REQUIRED data if not provided, such as the new version number or repository link