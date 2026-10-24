# Vision · public content

Files the Vision app reads from the internet. The app's code is **not** here.

## The dragons

<!-- dragons:start -->
<table>
<tr><td align="center"><img src="gallery/purple.gif" width="96" alt="Ametista"><br><b>Ametista</b><br><sub>Seu primeiro guardião</sub></td><td align="center"><img src="gallery/emerald.gif" width="96" alt="Esmeralda"><br><b>Esmeralda</b><br><sub>Bata uma meta</sub></td><td align="center"><img src="gallery/ruby.gif" width="96" alt="Rubi"><br><b>Rubi</b><br><sub>O tesouro render R$ 100 no total</sub></td><td align="center"><img src="gallery/ice.gif" width="96" alt="Gelo"><br><b>Gelo</b><br><sub>O tesouro render R$ 1.000 no total</sub></td></tr>
</table>
<!-- dragons:end -->

| File | Purpose |
|---|---|
| `dialogue.json` | Lines of the dragon (by mood and by screen), of the ad goblin, and the dragons catalog. The app downloads it at most every 12 h; if the file is invalid it is ignored and the previous one stays. |
| `sprites/` | The purple dragon and the palette, used to draw the gallery above. |
| `privacidade.md` | Privacy policy (link required by the Play Store). With GitHub Pages on: `https://dungeondevlabs.github.io/Vision/privacidade` |

## dialogue.json rules
- Each line up to **120 characters**; no empty list; at most 500 lines in total.
- Lines are shown to users in Portuguese.
- The goblin **never** talks about the ad or asks for a click (AdMob policy: it gets the account banned).
- Validate the JSON before pushing (e.g. jsonlint.com). A broken file is ignored by the app, but better not to risk it.

## A new dragon (no app update)
Add it to `"dragons"` in `dialogue.json`:
```json
{"id": "gold", "name": "Ouro", "howToUnlock": "Assista a um vídeo", "unlock": "video",
 "colors": {"l": "w", "d": "y", "h": "g", "p": "f", "q": "u"}}
```
- `id`: lowercase letters only, unique. `name` up to 30 characters, `howToUnlock` up to 80.
- `unlock`: `"video"` (rewarded video) or `"milestone:<regex>"` over achievement keys
  (e.g. `milestone:acumulado-100000` = R$ 1.000 earned in total, `milestone:meta-\d+-100` = a goal reached).
- `colors`: which palette color (`sprites/palette.txt`) replaces which in the purple dragon:
  `l` body, `d` shadow, `h` highlight, `p`/`q` wings. Only palette characters are accepted.
- The gallery above is redrawn by GitHub Actions when the file changes.
