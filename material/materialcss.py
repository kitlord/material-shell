THEME_MODE = "dark"
# THEME_MODE = "light"

APP_FONT = "Roboto 11"

import json
from pathlib import Path

_MATERIAL_DIR = Path(__file__).resolve().parent
DEFAULT_COLORS_PATH = _MATERIAL_DIR / "colors.json"


def generate_material_css(theme_mode: str = THEME_MODE, colors_path: Path = DEFAULT_COLORS_PATH) -> str:
    with open(colors_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    colors = data.get("colors", {})
    css = ""
    
    shapes = {
        "none": "0px",
        "extra-small": "4px",
        "small": "8px",
        "medium": "12px",
        "large": "16px",
        "large-increased": "20px",
        "extra-large": "28px",
        "extra-large-increased": "32px",
        "extra-extra-large": "48px",
        "full": "9999px"
    }

    # Generate CSS for the selected theme mode
    css += f"/* {theme_mode.capitalize()} Theme */\n"
    css += "* { all: unset; background: transparent; border: none; padding: 0; margin: 0;}"
    css += ":root {\n"
        
    for name, value in colors.items():
        css_name = name.replace('_', '-')
        hex_color = value.get(theme_mode, {}).get("color", "")
        if hex_color:
            css += f"  --mt-{css_name}: {hex_color};\n"

    for name, value in shapes.items():
        css += f"  --mt-shape-{name}: {value};\n"

    css += "}\n\n"

    # Generate utility classes for backgrounds and text colors
    for name in colors.keys():
        css_name = name.replace('_', '-')
        css += f".--mt-{css_name} {{\n"

        if "on_" in name:
            css += f"  color: var(--mt-{css_name});\n"
            replaced_name = css_name.replace('on-', '')
            if replaced_name in colors:
                css += f"  background: var(--mt-{replaced_name});\n"
            # print(name, css_name, css_name.replace('on-', ''))
        else:
            if f"on_{name}" in colors:
                css += f"  color: var(--mt-on-{css_name});\n"
            css += f"  background: var(--mt-{css_name});\n"

        css += "  border: none;\n"
        css += "  padding: 0;\n"

        css += "}\n"

    # Generate utility classes for border radius
    for name in shapes.keys():
        css += f".--mt-shape-{name} {{\n"
        css += f"  border-radius: var(--mt-shape-{name});\n"
        css += "}\n\n"

    return css


# Backward-compatible alias
def generate_css():
    return generate_material_css()