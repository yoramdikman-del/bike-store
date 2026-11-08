# גרפיקה לפוסטי "המוצר של היום" לפי social/products/daily.json
# פלט: social/posts/product/<תאריך>-<מספר מוצר>.png
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
F = lambda w, s: ImageFont.truetype(os.path.join(HERE, f'Rubik-{w}.ttf'), s, layout_engine=ImageFont.Layout.RAQM)
W = 1080

def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def fix(t):
    # סימן + בסוף מילה לועזית (ANT+) נשאר צמוד אליה גם בטקסט מימין לשמאל
    return t.replace('+', '+\u200e')

def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f, direction='rtl'); return b[2] - b[0]

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if tw(d, t, f) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def make(p, prods):
    bg, fg, ac = hexrgb(p['bg']), hexrgb(p['fg']), hexrgb(p['accent'])
    im = Image.new('RGB', (W, W), bg); d = ImageDraw.Draw(im)
    # תגית
    f_tag = F(700, 34); tag = 'המוצר של היום'
    tw_ = tw(d, tag, f_tag); x1 = W - 60; x0 = x1 - tw_ - 48
    d.rounded_rectangle([x0, 50, x1, 106], 28, fill=ac)
    d.text((x1 - 24, 78), tag, font=f_tag, fill=bg if sum(ac) > 380 else (255, 255, 255), anchor='rm', direction='rtl')
    # כותרת
    size = 74
    while True:
        f_h = F(900, size); lines = wrap(d, p['head'], f_h, W - 120)
        if len(lines) <= 2 or size <= 54: break
        size -= 4
    y = 130
    for ln in lines:
        d.text((W - 60, y), ln, font=f_h, fill=fg, anchor='ra', direction='rtl'); y += int(size * 1.15)
    # כרטיס מוצר
    top, bottom = y + 20, 860
    d.rounded_rectangle([60, top, W - 60, bottom], 36, fill=(255, 255, 255))
    src = Image.open(os.path.join(ROOT, 'media', p['id'], f"img_{p['img']:02d}.jpg")).convert('RGB')
    box = (W - 120 - 40, bottom - top - 40)
    src.thumbnail(box, Image.LANCZOS)
    if src.width < box[0] * 0.6 and src.height < box[1] * 0.6:
        r = min(box[0] / src.width, box[1] / src.height); src = src.resize((int(src.width * r), int(src.height * r)), Image.LANCZOS)
    mask = Image.new('L', src.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, *src.size], 24, fill=255)
    im.paste(src, ((W - src.width) // 2, top + (bottom - top - src.height) // 2), mask)
    # שם המוצר
    pr = prods[p['id']]
    f_t = F(700, 34); title = fix(f"{pr['brand']} | {pr['title']}")
    while tw(d, title, f_t) > W - 120 and f_t.size > 24: f_t = F(700, f_t.size - 2)
    d.text((W - 60, 900), title, font=f_t, fill=fg, anchor='rm', direction='rtl')
    # צ'יפים
    f_c = F(700, 30); x = W - 60
    for c in map(fix, p['chips']):
        w = tw(d, c, f_c) + 40
        d.rounded_rectangle([x - w, 950, x, 1004], 27, outline=fg, width=3)
        d.text((x - 20, 977), c, font=f_c, fill=fg, anchor='rm', direction='rtl'); x -= w + 14
    # לוגו וכתובת
    logo = Image.open(os.path.join(ROOT, 'social', 'logo_1024.png')).convert('RGBA').resize((96, 96), Image.LANCZOS)
    im.paste(logo, (60, 30), logo)
    d.text((166, 78), 'myripo.com/bike-store', font=F(400, 24), fill=fg, anchor='lm')
    out = os.path.join(ROOT, 'social', 'posts', 'product', f"{p['date']}-{p['id']}.png")
    im.save(out, optimize=True); return out

if __name__ == '__main__':
    prods = {x['id']: x for x in json.load(open(os.path.join(ROOT, 'data', 'products.json'), encoding='utf-8'))['products']}
    days = json.load(open(os.path.join(HERE, 'daily.json'), encoding='utf-8'))
    only = sys.argv[1:]
    for p in days:
        if not only or p['date'] in only: print(make(p, prods))
