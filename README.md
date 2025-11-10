# AI Agent Prompts & Configurations

Welcome to my personal, curated collection of prompts, modes, and configurations for AI coding assistants. This repository is designed for anyone interested in **Prompt Engineering**, customizing **AI Agents**, or enhancing their workflow with Large Language Models (LLMs).

This collection contains ready-to-use templates for defining agent personas, delegating tasks, and structuring interactions with various AI tools.

## Applicable Tools & Platforms

The configurations in this repository are designed to be highly adaptable and can be used with a wide range of AI agent tools and platforms, including:

- **IDE Extensions:** Roo Code, Cline, Kilo Code, Cursor, Windsurf, Continue
- **Chat Platforms:** LibreChat, Open WebUI
- **APIs & CLIs:** Anthropic Claude Code, Google Gemini, OpenAI Codex/ChatGPT, OpenCode

While the principles are universal, the specific file paths and structures are optimized for **Roo Code**.

## Architecture: "Prompt-as-Code"

This repository uses a **Prompt Builder** system to manage agent modes. This approach treats prompt engineering as a development process, where configurations are generated from source files.

### Repository Structure

- **`/commands`**: Contains markdown templates for slash-commands, it's like copypaste.
  - `subtask-analysis.md`: A template for creating a research-focused sub-agent.
  - `subtask-code.md`: A template for creating a code-writing sub-agent.

- **`/prompt_builder`**: The source directory for agent modes.
  - `build.py`: A Python script that assembles all components into the final configuration file.
  - `manifest.yaml`: Defines which agent modes to include in the build.
  - `/sources`: Contains the raw materials (metadata and instructions) for each mode.

- **`custom_modes.yaml`**: The **generated output file** for agent modes. This file should not be edited manually, as it is overwritten by the build script.

## Configuration for Roo Code

The setup process involves two distinct types of assets: **Custom Modes** and **Custom Commands**.

### 1. Custom Modes

Custom modes are managed via the Prompt Builder workflow.

**Step 1: Edit the Sources**
All modifications to modes are done in the `/prompt_builder/sources` directory.
- To change a mode's instructions, edit its `prompt.md` file.
- To change a mode's metadata (e.g., name, description), edit its `config.yaml` file.
- To add a new mode, create a new sub-directory in `/sources` with the required files and add its name to `manifest.yaml`.

**Step 2: Build the Configuration File**
Run the build script from the repository's root directory to generate the final `custom_modes.yaml`:
```bash
python prompt_builder/build.py
```

**Step 3: Link the Output File**
The generated `custom_modes.yaml` is the file to be used by the AI agent. For Roo Code, place it at:
`C:\Users\<USER>\AppData\Roaming\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\custom_modes.yaml`

### 2. Custom Commands

Custom commands are managed by copying the templates directly.

To use the command templates, place the files from the `/commands` directory into:
`C:\Users\<USER>\.roo\commands\`

## Available Modes

This repository provides the following agent modes, forming the "Pantheon" team:

- **🧠 Maestro**: An expert project orchestrator who decomposes complex tasks, delegates them to specialist agents, and manages the overall project plan.
- **🏛️ Principal Engineer**: A top-tier technical leader for deep system analysis, architectural design, and long-term strategic planning.
- **💻 Lead Implementer**: An expert developer who translates architectural plans into clean, efficient, and maintainable application code.
- **🧪 Test Engineer**: A dedicated quality expert who writes clean, fast, and reliable unit and integration tests to ensure code correctness and robustness.
- **🎭 Advocate**: A user experience specialist who designs intuitive, enjoyable, and habit-forming user flows by applying principles of usability and psychology.
- **🌿 Gardener**: A meticulous engineer focused on code quality, fighting entropy by refactoring, updating dependencies, and eliminating technical debt.
- **👾 Mr. Robot**: A cybersecurity expert who performs security audits and finds unconventional, low-cost solutions by reverse-engineering and exploiting external systems.
- **👁️ Observer**: A performance and systems expert who makes applications transparent by instrumenting code with logs, metrics, and traces, and setting up deployment infrastructure.
- **👺 Annihilator**: A cynical but logical agent whose sole purpose is to challenge complexity and ruthlessly identify features, code, or concepts that should be removed to regain focus.