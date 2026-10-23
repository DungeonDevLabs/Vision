# Vision · public content

Files the Vision app reads from the internet. The app's code is **not** here.

| File | Purpose |
|---|---|
| `dialogue.json` | Lines of the dragon (by mood: Happy, Idle, Sleeping, Worried) and of the ad goblin. The app downloads it at most every 12 h; if the file is invalid it is ignored and the previous one stays. |
| `privacidade.md` | Privacy policy (link required by the Play Store). With GitHub Pages on: `https://dungeondevlabs.github.io/Vision/privacidade` |

## dialogue.json rules
- Each line up to **120 characters**; no empty list; at most 500 lines in total.
- Lines are shown to users in Portuguese.
- The goblin **never** talks about the ad or asks for a click (AdMob policy: it gets the account banned).
- Validate the JSON before pushing (e.g. jsonlint.com). A broken file is ignored by the app, but better not to risk it.
