#!/usr/bin/env python3
"""Makes the 1200x630 link-preview images in site/assets/og/. Run: python3 tools/make_og.py
Paper images: the whole cover, fitted to the height and centred on the cover's dark blue.
site.jpg: the default image for the main pages."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS = ROOT / "site" / "insights" / "papers"
OUT = ROOT / "site" / "assets" / "og"
OUT.mkdir(parents=True, exist_ok=True)
W, H, BG = 1200, 630, (12, 26, 52)
FONT = "/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"

for cover in sorted(PAPERS.glob("*-cover.jpg")):
    c = Image.open(cover).convert("RGB")
    c = c.crop((3, 3, c.width - 3, c.height - 3))  # drop light edge pixels
    scale = min(H / c.height, W / c.width)
    c = c.resize((round(c.width * scale), round(c.height * scale)), Image.LANCZOS)
    im = Image.new("RGB", (W, H), BG)
    im.paste(c, ((W - c.width) // 2, (H - c.height) // 2))
    im.save(OUT / cover.name.replace("-cover.jpg", ".jpg"), quality=88)

def font(size, weight):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_axes([min(max(size, 14), 32), weight])
    except Exception:
        pass
    return f

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
x = 96
d.rectangle([x, 150, x + 72, 156], fill=(39, 179, 234))
d.text((x, 190), "Collabor8\u2122", font=font(96, 800), fill=(242, 246, 251))
d.text((x, 320), "Complex problems, solved.", font=font(52, 700), fill=(39, 179, 234))
d.text((x, 410), "Senior management consulting  \u00b7  Dubai, UAE", font=font(30, 500), fill=(201, 213, 230))
d.text((x, 520), "collabor8.solutions", font=font(26, 500), fill=(138, 155, 181))
im.save(OUT / "site.jpg", quality=90)
print("made", len(list(OUT.glob("*.jpg"))), "images")
