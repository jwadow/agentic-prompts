# "Prompt-as-Code" Management System Architecture

## 1. Context and Problem

As the number of custom roles (modes) for the AI agent grows, managing their prompts becomes a complex task. Manual editing of multiple files leads to duplication, errors, and maintenance difficulties.

## 2. Solution: "Prompt-as-Code" Architecture

This architecture prioritizes **simplicity and ease of use**, relying on **conventions** over complex **configuration**.

**Core Idea:** We maintain an automated build process but radically simplify the source file structure. Editing a single role now only requires working with one instruction file.

The system automatically generates the main `custom_modes.yaml` configuration file.

## 3. Detailed Architecture Structure

### 3.1. Directory Structure

```
.
├── roles_builder/
│   ├── manifest.yaml              # Manages the order of roles
│   ├── sources/
│   │   ├── _shared/
│   │   │   └── common_header.md   # Single file for shared instructions
│   │   │
│   │   ├── principal_engineer/
│   │   │   ├── config.yaml        # ONLY metadata (slug, name, etc.)
│   │   │   └── prompt.md          # ALL instructions for the role in one file
│   │   │
│   │   └── ... (other roles)
│   │
│   └── build.py                     # Simplified, convention-based script
│
└── custom_modes.yaml                 # Output .yaml file
```

### 3.2. Key Components

#### `roles_builder/manifest.yaml`
- **Purpose:** Defines which roles are included in the build and in what order. This is the only file that needs to be edited to manage the order.
- **Example:**
  ```yaml
  roles:
    - principal-engineer
    - test-engineer
  ```

#### `sources/{role_name}/config.yaml`
- **Purpose:** The single source of truth for a role's metadata. Contains all fields that will go into `custom_modes.yaml`, except for `customInstructions`.
- **Feature:** Long text fields like `roleDefinition` and `whenToUse` should be formatted as multi-line blocks for readability.
- **Example:**
  ```yaml
  slug: principal-engineer
  name: 🏛️ Principal Engineer
  description: Deep analysis, architectural design, strategy (@jwadow)
  roleDefinition: |
    You are a Principal Engineer, a top-tier technical leader.
    Your expertise is in deep system analysis...
  whenToUse: |
    Use this mode for brainstorm, deep architectural analysis...
  source: global
  groups:
    - read
  ```

#### `sources/{role_name}/prompt.md`
- **Purpose:** Contains **only** the role-specific instructions that will be added to `customInstructions`.
- **Example:**
  ```markdown
  ### Core Principles of a Principal Engineer (@jwadow)
  ...
  ```

#### `sources/_shared/common_header.md`
- **Purpose:** Contains common instructions that are automatically added to the beginning of `customInstructions` for **every** role.

### 3.3. Build Script `build.py` (Convention-based Logic)

- **Purpose:** Automates the build process.
- **Final Logic (Manual YAML Generation):**
  1.  Reads `manifest.yaml` to get the order of roles.
  2.  Collects all data from `config.yaml` for each role.
  3.  Dynamically generates a block with the team description.
  4.  For each role, assembles the final `customInstructions` from the dynamic block, `_shared/common_header.md`, and the role's `prompt.md`.
  5.  **Instead of using the `PyYAML` library for writing**, the script manually generates the final `custom_modes.yaml` line by line as a text file. This provides 100% control over indentation, line breaks, and the formatting of multi-line blocks (`|`), ensuring a perfect and predictable result.
  6.  Writes the final `custom_modes.yaml`.

## 4. Workflow

### Adding a New Role
1.  Create a folder for the role in `roles_builder/sources/`.
2.  Inside, create `config.yaml` (with metadata) and `prompt.md` (with instructions).
3.  Add the role's `slug` to `roles_builder/manifest.yaml`.
4.  Run `python roles_builder/build.py`.

### Modifying a Role
-   To change instructions, edit `sources/{role_name}/prompt.md`.
-   To change metadata, edit `sources/{role_name}/config.yaml`.

### Modifying Common Instructions
-   Edit `sources/_shared/common_header.md`.