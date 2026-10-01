<div align="center">

<img src="ascii_art.svg" width="700" alt="ASCII art">

# monkeytype_cheat

A small Python bot that opens [Monkeytype](https://monkeytype.com) and types the words for you.

</div>

## How it works

It uses [Playwright](https://playwright.dev/python/) to open Monkeytype in a browser, reads the current active word from the page, types it, presses space, and repeats until the test is over.

## Run it

```bash
pip install playwright
playwright install chromium
python main.py
```

Replace `main.py` with the name of your script. When the test is done, press Enter in the terminal to close the browser.

## Disclaimer

Made for learning how browser automation works. Don't use it to cheat on leaderboards or in competitions.
