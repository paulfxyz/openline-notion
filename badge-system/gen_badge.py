#!/usr/bin/env python3
"""
Openline OS — Badge Generator (sustainable, reusable)
-----------------------------------------------------
Renders flat "pill" badges that match the existing os-nav badge style:
  - rounded-pill shape, solid fill
  - small white line-icon on the left
  - bold white UPPERCASE text with letter-spacing
  - 34px tall (rendered at 3x then downsampled for crisp edges)

Usage:
  python3 gen_badge.py <label> <slug> [color] [icon]

  color: hex like #312E81  OR a named palette key (navy, gold, purple,
         emerald, cyan, violet, slate, rose, teal, orange)
  icon : a glyph name from ICONS (see below) or 'none'

Examples:
  python3 gen_badge.py "Read & Last Activity" badge-read-last-activity navy eye
  python3 gen_badge.py "Quick Actions" badge-quick-actions violet bolt

Batch: import build_badge() and call it in a loop (see gen_all.py).
"""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
S = 3                      # supersample factor
H = 34                     # final height in px
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Palette sampled from the existing badges
PALETTE = {
    "navy":    "#312E81",  # indigo-900  (Executive / strategic)
    "gold":    "#B47809",  # amber-700   (tips / prod / why-this-exists)
    "purple":  "#86198F",  # fuchsia-800 (badge-system)
    "emerald": "#047857",  # emerald-700 (golden rule)
    "cyan":    "#0E7490",  # cyan-700    (ai agent)
    "violet":  "#6D28D9",  # violet-700  (how-it-works)
    "slate":   "#334155",
    "rose":    "#9F1239",
    "teal":    "#0F766E",
    "orange":  "#C2410C",
    "blue":    "#1D4ED8",
    "pink":    "#BE185D",
    # --- extended palette (deep, saturated, white-text safe) ---
    "red":       "#B91C1C",  # red-700
    "crimson":   "#9F1239",  # rose-800
    "maroon":    "#7F1D1D",  # red-900
    "amber":     "#B45309",  # amber-700
    "bronze":    "#92400E",  # amber-800
    "olive":     "#4D7C0F",  # lime-700
    "green":     "#15803D",  # green-700
    "forest":    "#166534",  # green-800
    "jade":      "#059669",  # emerald-600
    "turquoise": "#0D9488",  # teal-600
    "sky":       "#0369A1",  # sky-700
    "azure":     "#0284C7",  # sky-600
    "cobalt":    "#1E40AF",  # blue-800
    "indigo":    "#4338CA",  # indigo-700
    "iris":      "#4F46E5",  # indigo-600
    "grape":     "#7E22CE",  # purple-700
    "plum":      "#6B21A8",  # purple-800
    "magenta":   "#A21CAF",  # fuchsia-700
    "fuchsia":   "#C026D3",  # fuchsia-600
    "raspberry": "#BE123C",  # rose-700
    "coral":     "#EA580C",  # orange-600
    "rust":      "#9A3412",  # orange-800
    "charcoal":  "#1F2937",  # gray-800
    "steel":     "#475569",  # slate-600
    "gunmetal":  "#0F172A",  # slate-900
}

def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ---- Minimal white line-icons drawn with primitives (scale-aware) ----
# Each fn draws into `d` inside a box (x0,y0,x1,y1) using stroke width lw.
def _eye(d, b, lw, col):
    x0,y0,x1,y1 = b; cx=(x0+x1)/2; cy=(y0+y1)/2; rw=(x1-x0)/2; rh=(y1-y0)/2.6
    # almond shape via two arcs -> approximate with ellipse outline
    d.ellipse([cx-rw, cy-rh, cx+rw, cy+rh], outline=col, width=lw)
    d.ellipse([cx-rh*0.6, cy-rh*0.6, cx+rh*0.6, cy+rh*0.6], fill=col)

def _bolt(d, b, lw, col):
    x0,y0,x1,y1 = b; w=x1-x0; h=y1-y0
    pts=[(x0+w*0.55,y0),(x0+w*0.15,y0+h*0.58),(x0+w*0.45,y0+h*0.58),
         (x0+w*0.35,y1),(x0+w*0.9,y0+h*0.4),(x0+w*0.55,y0+h*0.4)]
    d.polygon(pts, fill=col)

def _gear(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2; cy=(y0+y1)/2; R=min(x1-x0,y1-y0)/2
    for i in range(8):
        a=math.radians(i*45)
        d.line([cx+math.cos(a)*R*0.55, cy+math.sin(a)*R*0.55,
                cx+math.cos(a)*R, cy+math.sin(a)*R], fill=col, width=lw)
    d.ellipse([cx-R*0.6,cy-R*0.6,cx+R*0.6,cy+R*0.6], outline=col, width=lw)

def _bulb(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2; w=x1-x0; h=y1-y0
    d.ellipse([cx-w*0.35, y0, cx+w*0.35, y0+h*0.7], outline=col, width=lw)
    d.line([cx-w*0.18, y0+h*0.8, cx+w*0.18, y0+h*0.8], fill=col, width=lw)
    d.line([cx-w*0.13, y1, cx+w*0.13, y1], fill=col, width=lw)

def _dollar(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2
    fnt=ImageFont.truetype(FONT_PATH, int((y1-y0)*1.15))
    d.text((cx, (y0+y1)/2), "$", font=fnt, fill=col, anchor="mm")

def _search(d, b, lw, col):
    x0,y0,x1,y1=b; r=(x1-x0)*0.34
    d.ellipse([x0, y0, x0+2*r, y0+2*r], outline=col, width=lw)
    d.line([x0+2*r*0.78, y0+2*r*0.78, x1, y1], fill=col, width=int(lw*1.2))

def _mail(d, b, lw, col):
    x0,y0,x1,y1=b
    d.rectangle([x0,y0,x1,y1], outline=col, width=lw)
    d.line([x0,y0,(x0+x1)/2,(y0+y1)/2], fill=col, width=lw)
    d.line([x1,y0,(x0+x1)/2,(y0+y1)/2], fill=col, width=lw)

def _globe(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2; cy=(y0+y1)/2
    d.ellipse([x0,y0,x1,y1], outline=col, width=lw)
    d.ellipse([cx-(x1-x0)*0.22,y0,cx+(x1-x0)*0.22,y1], outline=col, width=lw)
    d.line([x0,cy,x1,cy], fill=col, width=lw)

def _building(d, b, lw, col):
    x0,y0,x1,y1=b
    d.rectangle([x0,y0,x1,y1], outline=col, width=lw)
    for fy in (0.28,0.55,0.82):
        for fx in (0.28,0.62):
            yy=y0+(y1-y0)*fy; xx=x0+(x1-x0)*fx
            d.rectangle([xx-1.4*lw,yy-1.4*lw,xx+1.4*lw,yy+1.4*lw], fill=col)

def _rocket(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2; w=x1-x0; h=y1-y0
    d.polygon([(cx,y0),(cx+w*0.3,y0+h*0.6),(cx-w*0.3,y0+h*0.6)], outline=col, width=lw)
    d.ellipse([cx-w*0.1,y0+h*0.25,cx+w*0.1,y0+h*0.45], fill=col)
    d.line([cx-w*0.18,y0+h*0.6,cx-w*0.3,y1], fill=col, width=lw)
    d.line([cx+w*0.18,y0+h*0.6,cx+w*0.3,y1], fill=col, width=lw)

def _code(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2; cy=(y0+y1)/2
    d.line([(x0+ (x1-x0)*0.32,y0),(x0,cy),(x0+(x1-x0)*0.32,y1)], fill=col, width=lw, joint="curve")
    d.line([(x1-(x1-x0)*0.32,y0),(x1,cy),(x1-(x1-x0)*0.32,y1)], fill=col, width=lw, joint="curve")

def _plug(d, b, lw, col):
    x0,y0,x1,y1=b; cx=(x0+x1)/2
    d.rectangle([cx-(x1-x0)*0.28,y0+ (y1-y0)*0.25,cx+(x1-x0)*0.28,y1-(y1-y0)*0.15], outline=col, width=lw)
    d.line([cx-(x1-x0)*0.12,y0,cx-(x1-x0)*0.12,y0+(y1-y0)*0.25], fill=col, width=lw)
    d.line([cx+(x1-x0)*0.12,y0,cx+(x1-x0)*0.12,y0+(y1-y0)*0.25], fill=col, width=lw)

def _puzzle(d, b, lw, col):
    x0,y0,x1,y1=b
    d.rectangle([x0,y0+(y1-y0)*0.15,x1,y1], outline=col, width=lw)
    d.ellipse([(x0+x1)/2-(x1-x0)*0.16,y0,(x0+x1)/2+(x1-x0)*0.16,y0+(y1-y0)*0.3], fill=col)

def _swap(d, b, lw, col):  # price comparison / swap arrows
    x0,y0,x1,y1=b; cy=(y0+y1)/2
    d.line([x0,y0+(y1-y0)*0.32,x1,y0+(y1-y0)*0.32], fill=col, width=lw)
    d.line([x1,y0+(y1-y0)*0.32,x1-(x1-x0)*0.25,y0], fill=col, width=lw)
    d.line([x1,y1-(y1-y0)*0.32,x0,y1-(y1-y0)*0.32], fill=col, width=lw)
    d.line([x0,y1-(y1-y0)*0.32,x0+(x1-x0)*0.25,y1], fill=col, width=lw)

def _file(d, b, lw, col):
    x0,y0,x1,y1=b
    d.polygon([(x0,y0),(x1-(x1-x0)*0.3,y0),(x1,y0+(y1-y0)*0.3),(x1,y1),(x0,y1)], outline=col, width=lw)
    for fy in (0.5,0.68,0.86):
        d.line([x0+(x1-x0)*0.2,y0+(y1-y0)*fy,x1-(x1-x0)*0.2,y0+(y1-y0)*fy], fill=col, width=max(1,int(lw*0.8)))

ICONS = {
    "eye": _eye, "bolt": _bolt, "gear": _gear, "bulb": _bulb, "dollar": _dollar,
    "search": _search, "mail": _mail, "globe": _globe, "building": _building,
    "rocket": _rocket, "code": _code, "plug": _plug, "puzzle": _puzzle,
    "swap": _swap, "file": _file,
}

def build_badge(label, slug, color="navy", icon="none", out_dir=OUT_DIR):
    fill = PALETTE.get(color, color)
    rgb = hex2rgb(fill)
    text = label.upper()

    h = H * S
    pad_x = 11 * S
    icon_box = 12 * S
    icon_gap = 6 * S
    tracking = 0.4 * S           # letter-spacing
    radius = 6 * S            # gentle rounded-rectangle corners (was h/2 full pill)

    font_size = 12 * S
    font = ImageFont.truetype(FONT_PATH, font_size)

    # measure text width with tracking
    tmp = Image.new("RGBA", (10, 10))
    td = ImageDraw.Draw(tmp)
    def text_w(s):
        w = 0
        for ch in s:
            bb = td.textbbox((0, 0), ch, font=font)
            w += (bb[2] - bb[0]) + tracking
        return w - tracking if s else 0
    tw = text_w(text)
    ascent, descent = font.getmetrics()

    has_icon = icon in ICONS
    left = pad_x
    content_w = (icon_box + icon_gap if has_icon else 0) + tw
    w = int(left * 2 + content_w)

    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=rgb + (255,))

    cx = left
    if has_icon:
        iy0 = (h - icon_box) / 2
        ICONS[icon](d, (cx, iy0, cx + icon_box, iy0 + icon_box), max(2, int(2.0 * S)), (255, 255, 255, 255))
        cx += icon_box + icon_gap

    # draw text with tracking, vertically centered
    ty = (h - (ascent + descent)) / 2
    for ch in text:
        d.text((cx, ty), ch, font=font, fill=(255, 255, 255, 255))
        bb = td.textbbox((0, 0), ch, font=font)
        cx += (bb[2] - bb[0]) + tracking

    final = img.resize((round(w / S), H), Image.LANCZOS)
    path = os.path.join(out_dir, slug + ".png")
    final.save(path)
    return path, final.size

if __name__ == "__main__":
    label = sys.argv[1]
    slug = sys.argv[2]
    color = sys.argv[3] if len(sys.argv) > 3 else "navy"
    icon = sys.argv[4] if len(sys.argv) > 4 else "none"
    p, sz = build_badge(label, slug, color, icon)
    print("wrote", p, sz)
