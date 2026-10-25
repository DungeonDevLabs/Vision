# Vision · Dungeon Dev Labs

**English** · [Português](#português)

Vision is a personal finance app for Android with a pixel-art dragon that guards your treasure.
This repository holds only the files the app reads from the internet; the app's code is **not** here.

## The dragons

<!-- dragons:start -->
<table>
<tr><td align="center"><img src="gallery/purple.gif" width="96" alt="Amethyst"><br><b>Amethyst</b> · Ametista<br><sub>Your first guardian</sub></td><td align="center"><img src="gallery/emerald.gif" width="96" alt="Emerald"><br><b>Emerald</b> · Esmeralda<br><sub>Reach a goal</sub></td><td align="center"><img src="gallery/ruby.gif" width="96" alt="Ruby"><br><b>Ruby</b> · Rubi<br><sub>The treasure earns R$ 100 in total</sub></td><td align="center"><img src="gallery/ice.gif" width="96" alt="Ice"><br><b>Ice</b> · Gelo<br><sub>The treasure earns R$ 1,000 in total</sub></td></tr>
</table>
<!-- dragons:end -->

## Files

| File | Purpose |
|---|---|
| `dialogue.json` / `dialogue.en.json` | Dragon lines (by mood and by screen), the ad goblin's lines and the dragons catalog, in Portuguese and English. The app downloads its language's file at most every 12 h; an invalid file is ignored and the previous one stays. |
| `banks.json` | How to read each bank's notifications (regex) to log expenses on their own. Same 12 h and same rule for invalid files. |
| `sprites/` | The purple dragon and the palette, used to draw the gallery above. |
| `privacidade.md` / `privacy.md` | Privacy policy (link required by the Play Store). |

## Rules for the dialogue files
- Each line up to **120 characters**; no empty list; at most 500 lines in total.
- Both files must have the same moods, screens and dragons (ids and colors).
- The goblin **never** talks about the ad or asks for a click (AdMob policy: it gets the account banned).
- Validate the JSON before pushing (e.g. jsonlint.com). A broken file is ignored by the app, but better not to risk it.

## A new dragon (no app update)
Add it to `"dragons"` in **both** files, with the same `id` and `colors` and the text in each language:
```json
{"id": "gold", "name": "Gold", "howToUnlock": "Watch a video", "unlock": "video",
 "colors": {"l": "w", "d": "y", "h": "g", "p": "f", "q": "u"}}
```
- `id`: lowercase letters only, unique. `name` up to 30 characters, `howToUnlock` up to 80.
- `unlock`: `"video"` (rewarded video) or `"milestone:<regex>"` over achievement keys
  (e.g. `milestone:acumulado-100000` = R$ 1,000 earned in total, `milestone:meta-\\d+-100` = a goal reached).
- `colors`: which palette color (`sprites/palette.txt`) replaces which in the purple dragon:
  `l` body, `d` shadow, `h` highlight, `p`/`q` wings. Only palette characters are accepted.
- The gallery above is redrawn by GitHub Actions when the files change.

## A new achievement (no app update)
Add it to `"achievements"` in **both** files, with the same `id`, `kind` and `value`:
```json
{"id": "five-chests", "name": "Hoarder", "description": "Have 5 chests", "kind": "baus", "value": 5, "icon": "📦"}
```
- `id`: lowercase letters, digits and `-`, unique. `name` up to 30 characters, `description` up to 80.
- `kind` and `value`: `rendimento` (net yield since the start, in cents), `patrimonio` (worth of the chests, in cents),
  `sequencia` (months in a row saving), `liberdade` (% of the fixed expenses the yield pays), `reserva` (months the
  emergency fund covers), `metas` (goals reached), `baus` (chests created), `desejos` (wishes bought).
- Once reached it stays unlocked. A dragon can unlock with it: `"unlock": "milestone:conquista-five-chests"`.

## Bank notifications (banks.json)
Each template lists the bank's app ids (`packages`) and regexes over the notification's title + text. Group `valor` is the
amount (`1.234,56`), the optional group `loja` is the description; `"income": true` means money in (a Pix received).
Shared sets (`sets`) hold the common patterns and a bank uses them with `"use": ["compras", "pix"]`.
```json
{"id": "nubank", "name": "Nubank", "packages": ["com.nu.production"], "use": ["compras", "pix"],
 "patterns": [{"regex": "(?i)compra de R\$\s?(?<valor>[\d.]+,\d{2}) aprovada em (?<loja>.+)"}]}
```
- A bank changed its wording? In the app, Settings › Spending tracker lists the bank notifications it didn't understand:
  copy one, fix or add a regex here, and the app picks it up within 12 h.
- Patterns are tried in order: the bank's own `patterns`, then each `use` set. Keep the most specific first.

## Community
Bugs, ideas, dragon skins and tips: [r/VisionDungeon](https://www.reddit.com/r/VisionDungeon).

---

## Português

O Vision é um app de finanças pessoais para Android com um dragão em pixel art que guarda o seu tesouro.
Este repositório tem só os arquivos que o app lê da internet; o código do app **não** fica aqui.

### Arquivos
| Arquivo | Para quê |
|---|---|
| `dialogue.json` / `dialogue.en.json` | Falas do dragão (por humor e por tela), do goblin do anúncio e o catálogo de dragões, em português e inglês. O app baixa o do seu idioma no máximo a cada 12 h; arquivo inválido é ignorado e o anterior continua. |
| `banks.json` | Como ler as notificações de cada banco (regex) para lançar gastos sozinho. Mesmas 12 h e mesma regra para arquivo inválido. |
| `sprites/` | O dragão roxo e a paleta, usados para desenhar a galeria acima. |
| `privacidade.md` / `privacy.md` | Política de privacidade (link exigido pela Play Store). |

### Regras das falas
- Cada fala com até **120 caracteres**; nenhuma lista vazia; no máximo 500 falas no total.
- Os dois arquivos precisam ter os mesmos humores, telas e dragões (ids e cores).
- O goblin **nunca** fala do anúncio nem pede clique (regra do AdMob: bane a conta).
- Valide o JSON antes de subir (ex.: jsonlint.com).

### Um dragão novo (sem atualizar o app)
Adicione em `"dragons"` nos **dois** arquivos, com o mesmo `id` e `colors` e o texto em cada idioma:
```json
{"id": "gold", "name": "Ouro", "howToUnlock": "Assista a um vídeo", "unlock": "video",
 "colors": {"l": "w", "d": "y", "h": "g", "p": "f", "q": "u"}}
```
- `unlock`: `"video"` (vídeo premiado) ou `"milestone:<regex>"` sobre as chaves de conquista.
- `colors`: qual cor da paleta (`sprites/palette.txt`) troca qual no dragão roxo: `l` corpo, `d` sombra, `h` brilho, `p`/`q` asas.
- A galeria acima é redesenhada pelo GitHub Actions quando os arquivos mudam.

### Uma conquista nova (sem atualizar o app)
Adicione em `"achievements"` nos **dois** arquivos, com o mesmo `id`, `kind` e `value`:
```json
{"id": "cinco-baus", "name": "Acumulador", "description": "Ter 5 baús", "kind": "baus", "value": 5, "icon": "📦"}
```
- `kind` e `value`: `rendimento` (rendimento líquido desde o começo, em centavos), `patrimonio` (valor dos baús, em centavos),
  `sequencia` (meses seguidos guardando), `liberdade` (% dos gastos fixos que o rendimento paga), `reserva` (meses que a
  reserva cobre), `metas` (metas batidas), `baus` (baús criados), `desejos` (desejos comprados).
- Depois de liberada, fica liberada. Um dragão pode depender dela: `"unlock": "milestone:conquista-cinco-baus"`.

### Notificações dos bancos (banks.json)
Cada modelo tem os ids dos apps do banco (`packages`) e regex sobre o título + texto da notificação. O grupo `valor` é o
valor (`1.234,56`), o grupo opcional `loja` é a descrição; `"income": true` é dinheiro entrando (Pix recebido).
Os conjuntos compartilhados (`sets`) têm os padrões comuns, e o banco usa com `"use": ["compras", "pix"]`.
- O banco mudou o texto? No app, em Ajustes › Controle de gastos, aparecem as notificações do banco que ele não entendeu:
  copie uma, ajuste ou crie uma regex aqui, e o app pega em até 12 h.

### Comunidade
Bugs, ideias, skins de dragão e dicas: [r/VisionDungeon](https://www.reddit.com/r/VisionDungeon).
