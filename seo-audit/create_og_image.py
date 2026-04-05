"""Generate OG social sharing image (1200x630) for Create Allied Health Services."""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = r"C:\Users\zacen\.claude\skills\canvas-design\canvas-fonts"
OUT = r"C:\Users\zacen\Python\vibe_coding\allied_health\images\og-image.png"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

W, H = 1200, 630

# Coastal Calm palette
STEEL_BLUE = "#3A6B8C"
STEEL_DARK = "#2C5570"
TERRACOTTA = "#C47A5A"
MUSTARD = "#D4A843"
LINEN = "#FBF7F2"
CHARCOAL = "#2A2F33"

img = Image.new("RGB", (W, H), STEEL_DARK)
draw = ImageDraw.Draw(img)

# Background gradient effect — darker left, lighter right
for x in range(W):
    r = int(44 + (58 - 44) * (x / W))
    g = int(85 + (107 - 85) * (x / W))
    b = int(112 + (140 - 112) * (x / W))
    draw.line([(x, 0), (x, H)], fill=(r, g, b))

# Decorative terracotta accent bar at top
draw.rectangle([(0, 0), (W, 6)], fill=TERRACOTTA)

# Decorative mustard accent line at bottom
draw.rectangle([(0, H - 4), (W, H)], fill=MUSTARD)

# Left side decorative element — terracotta vertical bar
draw.rectangle([(60, 160), (66, 470)], fill=TERRACOTTA)

# Brand mark "C" circle
cx, cy, cr = 110, 315, 40
draw.ellipse([(cx - cr, cy - cr), (cx + cr, cy + cr)], fill=LINEN)
f_mark = font("Lora-Bold.ttf", 38)
mark_bbox = draw.textbbox((0, 0), "C", font=f_mark)
mark_w = mark_bbox[2] - mark_bbox[0]
mark_h = mark_bbox[3] - mark_bbox[1]
draw.text((cx - mark_w // 2, cy - mark_h // 2 - 4), "C", fill=STEEL_DARK, font=f_mark)

# Main content area
content_x = 180

# Eyebrow
f_eyebrow = font("InstrumentSans-Bold.ttf", 14)
draw.text((content_x, 180), "NDIS REGISTERED PROVIDER  |  SYDNEY, AUSTRALIA", fill=TERRACOTTA, font=f_eyebrow)

# Brand name
f_brand = font("Lora-Bold.ttf", 52)
draw.text((content_x, 215), "Create Allied Health", fill=LINEN, font=f_brand)

# Sub brand
f_sub = font("InstrumentSans-Regular.ttf", 24)
draw.text((content_x, 280), "Services", fill="#9BBAD0", font=f_sub)

# Divider
draw.rectangle([(content_x, 325), (content_x + 80, 327)], fill=TERRACOTTA)

# Tagline
f_tagline = font("Lora-Italic.ttf", 26)
draw.text((content_x, 350), "Empower Your Journey", fill=LINEN, font=f_tagline)

# Services line
f_services = font("InstrumentSans-Regular.ttf", 16)
draw.text(
    (content_x, 400),
    "Psychosocial Assessment  |  Hospital Discharge  |  Housing Support",
    fill="#9BBAD0",
    font=f_services,
)
draw.text(
    (content_x, 425),
    "Guardianship & NCAT  |  Aged Care  |  Mental Health  |  Clinical Supervision",
    fill="#9BBAD0",
    font=f_services,
)

# Contact info
f_contact = font("InstrumentSans-Bold.ttf", 18)
draw.text((content_x, 480), "1800 930 350", fill=MUSTARD, font=f_contact)

f_url = font("InstrumentSans-Regular.ttf", 15)
draw.text((content_x + 180, 482), "createalliedhealth.com.au", fill="#9BBAD0", font=f_url)

# Right side — decorative abstract shapes
# Large circle (steel blue lighter)
draw.ellipse([(900, 80), (1150, 330)], fill="#4A7D9E", outline=None)
draw.ellipse([(920, 100), (1130, 310)], fill=None, outline=TERRACOTTA, width=1)

# Smaller overlapping circle
draw.ellipse([(980, 280), (1180, 480)], fill="#3D7292", outline=None)

# Tiny accent dot
draw.ellipse([(880, 350), (900, 370)], fill=MUSTARD)

# Another small element
draw.ellipse([(1100, 450), (1130, 480)], fill=TERRACOTTA)

img.save(OUT, "PNG", quality=95)
print(f"Saved: {OUT}")
print(f"Size: {os.path.getsize(OUT) / 1024:.0f} KB")
