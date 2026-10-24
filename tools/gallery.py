"""Draws every dragon of dialogue.json as an animated GIF and rewrites the gallery in README.md.

Run by .github/workflows/gallery.yml whenever dialogue.json changes; locally: pip install pillow && python tools/gallery.py
Each dragon is the purple one (sprites/dragon_idle.txt) with its "colors" swapped, exactly like the app draws it.
"""
import json
import os
import re

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALE = 6
START, END = '<!-- dragons:start -->', '<!-- dragons:end -->'


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as fh:
        return fh.read()


def palette():
    out = {}
    for line in read('sprites/palette.txt').splitlines():
        if line.strip():
            char, hex_ = line.split()
            out[char] = tuple(int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return out


def frames(text):
    fps = int(re.search(r'^fps:\s*(\d+)', text, re.M).group(1))
    out, current = [], None
    for line in text.splitlines():
        if line.startswith('---'):
            current = []
            out.append(current)
        elif current is not None and line:
            current.append(line)
    return out, fps


def gif(path, rows_list, fps, colors, swap):
    images = []
    for rows in rows_list:
        img = Image.new('RGBA', (len(rows[0]), len(rows)), (0, 0, 0, 0))
        for y, line in enumerate(rows):
            for x, c in enumerate(line):
                c = swap.get(c, c)
                if c != '.':
                    img.putpixel((x, y), colors[c] + (255,))
        images.append(img.resize((img.width * SCALE, img.height * SCALE), Image.NEAREST))
    images[0].save(path, save_all=True, append_images=images[1:], duration=1000 // fps, loop=0, disposal=2)


def main():
    data = json.loads(read('dialogue.json'))
    colors = palette()
    rows_list, fps = frames(read('sprites/dragon_idle.txt'))
    dragons = [{'id': 'purple', 'name': 'Ametista', 'howToUnlock': 'Seu primeiro guardião', 'colors': {}}] + data.get('dragons', [])
    os.makedirs(os.path.join(ROOT, 'gallery'), exist_ok=True)
    cells = []
    for d in dragons:
        swap = {k: v for k, v in d.get('colors', {}).items() if k in colors and v in colors}
        gif(os.path.join(ROOT, 'gallery', f"{d['id']}.gif"), rows_list, fps, colors, swap)
        cells.append(f'<td align="center"><img src="gallery/{d["id"]}.gif" width="96" alt="{d["name"]}"><br>'
                     f'<b>{d["name"]}</b><br><sub>{d["howToUnlock"]}</sub></td>')
    rows = ['<tr>' + ''.join(cells[i:i + 4]) + '</tr>' for i in range(0, len(cells), 4)]
    table = f'{START}\n<table>\n' + '\n'.join(rows) + f'\n</table>\n{END}'
    readme = read('README.md')
    readme = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: table, readme, flags=re.S)
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(readme)
    print(f'{len(dragons)} dragons')


if __name__ == '__main__':
    main()
