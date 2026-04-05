"""
Chromatic Cartography — Color Palette Poster for Create Allied Health Services
Three distinct theme directions, presented as a cartographic color map.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas dimensions (landscape)
W, H = 1920, 1080

# Font paths
FONT_DIR = r"C:\Users\zacen\.claude\skills\canvas-design\canvas-fonts"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

# Fonts
f_title = font("InstrumentSerif-Regular.ttf", 42)
f_title_italic = font("InstrumentSerif-Italic.ttf", 32)
f_section = font("InstrumentSans-Bold.ttf", 22)
f_palette_name = font("Lora-Bold.ttf", 28)
f_palette_sub = font("Lora-Italic.ttf", 16)
f_label = font("InstrumentSans-Regular.ttf", 13)
f_hex = font("GeistMono-Regular.ttf", 12)
f_desc = font("InstrumentSans-Regular.ttf", 14)
f_tiny = font("GeistMono-Regular.ttf", 10)
f_button = font("InstrumentSans-Bold.ttf", 13)
f_tagline = font("Lora-Italic.ttf", 14)

# Background
BG = "#F8F6F2"
RULE_COLOR = "#D5D0C8"
TEXT_DARK = "#2A2A2A"
TEXT_MID = "#6B6560"
TEXT_LIGHT = "#9B9590"

# Palettes
palettes = [
    {
        "name": "Warm Harbour",
        "subtitle": "Navy & Warm Gold",
        "desc": "Trust and authority anchored by warmth.\nPremium, grounded, deeply professional.",
        "colors": [
            ("#1B2A4A", "Primary", "Deep Navy"),
            ("#C4973B", "Secondary", "Warm Gold"),
            ("#E07A5F", "Accent", "Soft Coral"),
            ("#FAF6F0", "Background", "Warm Ivory"),
            ("#2D3436", "Text", "Charcoal"),
        ],
        "btn_bg": "#1B2A4A",
        "btn_fg": "#FAF6F0",
        "card_bg": "#FAF6F0",
        "card_border": "#1B2A4A",
        "card_accent": "#C4973B",
    },
    {
        "name": "Dusk Bloom",
        "subtitle": "Plum & Blush",
        "desc": "Wisdom and dignity wrapped in empathy.\nCalming, distinctive, clinically refined.",
        "colors": [
            ("#5B2C6F", "Primary", "Deep Plum"),
            ("#C77D8A", "Secondary", "Dusty Rose"),
            ("#D4A03C", "Accent", "Amber"),
            ("#F5F0F7", "Background", "Soft Lavender"),
            ("#2C2C3A", "Text", "Dark Slate"),
        ],
        "btn_bg": "#5B2C6F",
        "btn_fg": "#F5F0F7",
        "card_bg": "#F5F0F7",
        "card_border": "#5B2C6F",
        "card_accent": "#C77D8A",
    },
    {
        "name": "Coastal Calm",
        "subtitle": "Steel Blue & Terracotta",
        "desc": "Reliability meets Australian warmth.\nEarthy, natural, quietly confident.",
        "colors": [
            ("#3A6B8C", "Primary", "Steel Blue"),
            ("#C47A5A", "Secondary", "Terracotta"),
            ("#D4A843", "Accent", "Soft Mustard"),
            ("#FBF7F2", "Background", "Warm Linen"),
            ("#2A2F33", "Text", "Deep Charcoal"),
        ],
        "btn_bg": "#3A6B8C",
        "btn_fg": "#FBF7F2",
        "card_bg": "#FBF7F2",
        "card_border": "#3A6B8C",
        "card_accent": "#C47A5A",
    },
]

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# --- Header area ---
# Top rule
draw.line([(60, 60), (W - 60, 60)], fill=RULE_COLOR, width=1)

# Brand name
draw.text((60, 75), "Create Allied Health", fill=TEXT_DARK, font=f_title)

# Tagline
draw.text((60, 125), "Empower Your Journey", fill=TEXT_MID, font=f_tagline)

# Right-aligned label
label_r = "Colour Palette Exploration"
bbox = draw.textbbox((0, 0), label_r, font=f_title_italic)
draw.text((W - 60 - (bbox[2] - bbox[0]), 82), label_r, fill=TEXT_LIGHT, font=f_title_italic)

# Sub-label
sub_r = "Three Directions  /  No Green"
bbox2 = draw.textbbox((0, 0), sub_r, font=f_tiny)
draw.text((W - 60 - (bbox2[2] - bbox2[0]), 120), sub_r, fill=TEXT_LIGHT, font=f_tiny)

# Divider below header
draw.line([(60, 155), (W - 60, 155)], fill=RULE_COLOR, width=1)

# --- Three columns ---
col_margin = 60
col_gap = 40
col_w = (W - 2 * col_margin - 2 * col_gap) // 3
col_top = 180

for i, pal in enumerate(palettes):
    cx = col_margin + i * (col_w + col_gap)
    cy = col_top

    # Column number
    draw.text((cx, cy), f"0{i+1}", fill=TEXT_LIGHT, font=f_tiny)

    # Palette name
    draw.text((cx, cy + 18), pal["name"], fill=TEXT_DARK, font=f_palette_name)

    # Subtitle
    draw.text((cx, cy + 52), pal["subtitle"], fill=TEXT_MID, font=f_palette_sub)

    # Thin rule
    draw.line([(cx, cy + 78), (cx + col_w, cy + 78)], fill=RULE_COLOR, width=1)

    # Description
    desc_lines = pal["desc"].split("\n")
    dy = cy + 90
    for line in desc_lines:
        draw.text((cx, dy), line, fill=TEXT_MID, font=f_desc)
        dy += 20

    # --- Color swatches ---
    swatch_top = cy + 145
    swatch_h = 72
    swatch_gap = 8
    swatch_w = col_w

    for j, (hex_val, role, name) in enumerate(pal["colors"]):
        sy = swatch_top + j * (swatch_h + swatch_gap)

        # Main swatch rectangle
        draw.rounded_rectangle(
            [(cx, sy), (cx + swatch_w, sy + swatch_h)],
            radius=6,
            fill=hex_val,
        )

        # For light backgrounds, add a subtle border
        if hex_val in ("#FAF6F0", "#F5F0F7", "#FBF7F2"):
            draw.rounded_rectangle(
                [(cx, sy), (cx + swatch_w, sy + swatch_h)],
                radius=6,
                outline="#D5D0C8",
                width=1,
            )

        # Text on swatch — choose contrast color
        r_val = int(hex_val[1:3], 16)
        g_val = int(hex_val[3:5], 16)
        b_val = int(hex_val[5:7], 16)
        lum = 0.299 * r_val + 0.587 * g_val + 0.114 * b_val
        txt_color = "#FFFFFF" if lum < 140 else "#2A2A2A"

        # Role label (top-left of swatch)
        draw.text((cx + 14, sy + 10), role.upper(), fill=txt_color, font=f_label)

        # Color name (below role)
        draw.text((cx + 14, sy + 28), name, fill=txt_color, font=f_desc)

        # Hex code (bottom-right)
        hex_bbox = draw.textbbox((0, 0), hex_val, font=f_hex)
        hex_w = hex_bbox[2] - hex_bbox[0]
        draw.text(
            (cx + swatch_w - hex_w - 14, sy + swatch_h - 24),
            hex_val,
            fill=txt_color,
            font=f_hex,
        )

    # --- Mini component preview ---
    comp_top = swatch_top + 5 * (swatch_h + swatch_gap) + 15

    # Label
    draw.text((cx, comp_top), "COMPONENT PREVIEW", fill=TEXT_LIGHT, font=f_tiny)
    comp_top += 20

    # Mini card
    card_w = col_w
    card_h = 115
    draw.rounded_rectangle(
        [(cx, comp_top), (cx + card_w, comp_top + card_h)],
        radius=8,
        fill=pal["card_bg"],
        outline=pal["card_border"],
        width=1,
    )

    # Card accent bar at top
    draw.rounded_rectangle(
        [(cx, comp_top), (cx + card_w, comp_top + 5)],
        radius=0,
        fill=pal["card_accent"],
    )
    # Fix top corners
    draw.rounded_rectangle(
        [(cx, comp_top), (cx + card_w, comp_top + 8)],
        radius=8,
        fill=pal["card_accent"],
    )
    draw.rectangle(
        [(cx + 1, comp_top + 5), (cx + card_w - 1, comp_top + 8)],
        fill=pal["card_accent"],
    )

    # Card text
    card_text_color = pal["colors"][4][0]  # text color
    draw.text(
        (cx + 16, comp_top + 18),
        "Person-Centered Care",
        fill=pal["colors"][0][0],
        font=f_section,
    )
    draw.text(
        (cx + 16, comp_top + 46),
        "Collaborative, strength-based",
        fill=card_text_color,
        font=f_desc,
    )
    draw.text(
        (cx + 16, comp_top + 63),
        "support for complex needs",
        fill=card_text_color,
        font=f_desc,
    )

    # Button inside card
    btn_w = 130
    btn_h = 32
    btn_x = cx + 16
    btn_y = comp_top + card_h - 42
    draw.rounded_rectangle(
        [(btn_x, btn_y), (btn_x + btn_w, btn_y + btn_h)],
        radius=6,
        fill=pal["btn_bg"],
    )
    # Center button text
    btn_text = "Learn More"
    btn_bbox = draw.textbbox((0, 0), btn_text, font=f_button)
    btn_tw = btn_bbox[2] - btn_bbox[0]
    btn_th = btn_bbox[3] - btn_bbox[1]
    draw.text(
        (btn_x + (btn_w - btn_tw) // 2, btn_y + (btn_h - btn_th) // 2 - 1),
        btn_text,
        fill=pal["btn_fg"],
        font=f_button,
    )

    # Vertical separator (between columns, not after last)
    if i < 2:
        sep_x = cx + col_w + col_gap // 2
        draw.line(
            [(sep_x, col_top), (sep_x, comp_top + card_h + 10)],
            fill=RULE_COLOR,
            width=1,
        )

# --- Footer ---
footer_y = H - 50
draw.line([(60, footer_y), (W - 60, footer_y)], fill=RULE_COLOR, width=1)

draw.text(
    (60, footer_y + 12),
    "CREATE ALLIED HEALTH SERVICES  /  COLOUR EXPLORATION  /  2026",
    fill=TEXT_LIGHT,
    font=f_tiny,
)

note = "All palettes exclude green per brief"
nbbox = draw.textbbox((0, 0), note, font=f_tiny)
draw.text(
    (W - 60 - (nbbox[2] - nbbox[0]), footer_y + 12),
    note,
    fill=TEXT_LIGHT,
    font=f_tiny,
)

# Save
out_path = r"C:\Users\zacen\Python\vibe_coding\allied_health\seo-audit\colour-palette-exploration.png"
img.save(out_path, "PNG", dpi=(150, 150))
print(f"Saved: {out_path}")
