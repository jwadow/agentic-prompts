# AI Agent Prompts & Configurations

Welcome to my personal, curated collection of prompts, modes, and configurations for AI coding assistants. This repository is designed for anyone interested in **Prompt Engineering**, customizing **AI Agents**, or enhancing their workflow with Large Language Models (LLMs).

This collection contains ready-to-use templates for defining agent personas, delegating tasks, and structuring interactions with various AI tools.

## Applicable Tools & Platforms

The configurations in this repository are designed to be highly adaptable and can be used with a wide range of AI agent tools and platforms, including:

- **IDE Extensions:** Roo Code, Cline, Kilo Code, Cursor, Windsurf, Continue
- **Chat Platforms:** LibreChat, Open WebUI
- **APIs & CLIs:** Anthropic Claude Code, Google Gemini, OpenAI Codex/ChatGPT, OpenCode

While the principles are universal, the specific file paths and structures are optimized for **Roo Code**.

## Repository Structure

- **`/commands`**: Contains markdown templates for slash-commands, it's like copypaste.
  - `subtask-analysis.md`: A template for creating a research-focused sub-agent.
  - `subtask-code.md`: A template for creating a code-writing sub-agent.

- **`/modes`**: Contains raw detailed definitions for custom agent personas (modes, system prompts).
  - `mode_test-engineer.md`: A comprehensive definition for a "Test Engineer" agent.

- **`/roo`**: Contains a ready-to-use configuration with all `/modes` included specifically for the Roo Code assistant.
  - `custom_modes.yaml`: The primary file for defining and loading custom modes.

## Roo Code: Specific Configuration

These instructions are tailored for setting up with **Roo Code**.

### Custom Commands

To use the custom command templates, place the files from the `/commands` directory into:
`C:\Users\<USER>\.roo\commands\`

### Custom Modes (`custom_modes.yaml`)

To load the custom modes defined in this repository, your `custom_modes.yaml` file should be located at:
`C:\Users\<USER>\AppData\Roaming\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\custom_modes.yaml`

*Note: The `rooveterinaryinc.roo-cline` part might vary based on your specific installation.*

The raw markdown files in the `/modes` directory are referenced by `custom_modes.yaml` and do not need to be moved.