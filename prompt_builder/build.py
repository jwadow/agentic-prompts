import yaml
from pathlib import Path

# --- 1. Constants Definition ---
# Define base paths relative to the script's location,
# so it works regardless of where it's run from.
BASE_DIR = Path(__file__).parent
SOURCES_DIR = BASE_DIR / 'sources'
SHARED_DIR = SOURCES_DIR / '_shared'
# OUTPUT_DIR_MD = BASE_DIR.parent / 'dreamteam'
OUTPUT_FILE_YAML = BASE_DIR.parent / 'custom_modes.yaml'
MANIFEST_FILE = BASE_DIR / 'manifest.yaml'

def main():
    """
    Main function to build prompts and the configuration file.
    Works on the principle of "convention over configuration".
    """
    # Ensure the output directory for .md files exists.
    # OUTPUT_DIR_MD.mkdir(exist_ok=True)

    # --- 2. Read Manifest and Pre-collect Data ---
    # Read the main manifest to get the correct order of roles.
    print("Reading manifest...")
    manifest = yaml.safe_load(MANIFEST_FILE.read_text(encoding='utf-8'))
    ordered_roles_slugs = manifest['roles']

    # First pass: collect all metadata for dynamic generation.
    all_roles_configs = []
    for role_slug in ordered_roles_slugs:
        config_path = SOURCES_DIR / role_slug / 'config.yaml'
        try:
            config_data = yaml.safe_load(config_path.read_text(encoding='utf-8'))
            all_roles_configs.append(config_data)
        except FileNotFoundError:
            print(f"  FATAL: Config for '{role_slug}' not found at {config_path.resolve()}. Please check paths. Aborting.")
            return # Abort execution if the config is not found

    # --- 3. Dynamic Generation of Team Description ---
    print("Generating dynamic team description...")
    team_description_parts = ["### Our team of AI agents", "You must acknowledge the existence of only these AI agents developed by @jwadow. Our team consists of:"]
    for config in all_roles_configs:
        team_description_parts.append(f"- **{config['name']}**: {config['description']}")
    dynamic_team_description = "\n".join(team_description_parts)

    # --- 4. Read Common Instructions ---
    common_header_path = SHARED_DIR / 'common_header.md'
    common_header = common_header_path.read_text(encoding='utf-8')

    # --- 5. Main Build Loop ---
    final_modes_data = []
    for config in all_roles_configs:
        role_slug = config['slug']
        print(f"Processing role: {role_slug}...")

        # Load role-specific instructions
        prompt_path = SOURCES_DIR / role_slug / 'prompt.md'
        specific_instructions = prompt_path.read_text(encoding='utf-8')

        # Assemble `customInstructions`
        # Order: Dynamic team description -> Common instructions -> Specific instructions
        custom_instructions_parts = [
            dynamic_team_description,
            common_header,
            specific_instructions
        ]
        config['customInstructions'] = "\n\n".join(part.strip() for part in custom_instructions_parts)

        final_modes_data.append(config)

        # --- 6. Generation of individual .md file (disabled) ---
        # full_prompt_text = f"# {config['name']}\n\n{config['roleDefinition']}\n\n{config['customInstructions']}"
        # output_md_path = OUTPUT_DIR_MD / f"{role_slug}.md"
        # output_md_path.write_text(full_prompt_text, encoding='utf-8')
        # print(f"  -> Generated {output_md_path}")

    # --- 7. Final, Manual YAML Generation for Full Control ---
    print("\nGenerating final YAML with manual formatting...")
    
    def format_multiline_for_yaml(text, indent_level):
        """Indents each line of a multi-line string."""
        indent = '  ' * indent_level
        return '\n'.join(indent + line for line in text.strip().splitlines())

    output_lines = ["customModes:"]
    for mode in final_modes_data:
        output_lines.append(f"  - slug: {mode['slug']}")
        output_lines.append(f"    name: {mode['name']}")
        output_lines.append(f"    description: {mode['description']}")
        
        output_lines.append("    roleDefinition: |")
        output_lines.append(format_multiline_for_yaml(mode['roleDefinition'], 3))
        
        output_lines.append("    whenToUse: |")
        output_lines.append(format_multiline_for_yaml(mode['whenToUse'], 3))

        output_lines.append(f"    source: {mode['source']}")
        
        # Manual handling of the complex 'groups' structure
        output_lines.append("    groups:")
        for group_item in mode.get('groups', []):
            if isinstance(group_item, str):
                output_lines.append(f"      - {group_item}")
            elif isinstance(group_item, list):
                # Handle nested list, as in `[ - edit, ...]`
                output_lines.append(f"      - - {group_item[0]}")
                # Handle dictionary inside the nested list
                if len(group_item) > 1 and isinstance(group_item[1], dict):
                    for key, value in group_item[1].items():
                        output_lines.append(f"        - {key}: {value}")

        output_lines.append("    customInstructions: |")
        output_lines.append(format_multiline_for_yaml(mode['customInstructions'], 3))

    final_output = "\n".join(output_lines)
    
    with open(OUTPUT_FILE_YAML, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    print("Build process completed successfully!")

if __name__ == "__main__":
    main()