from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://monkeytype.com")

    page.wait_for_timeout(5000)

    while True:
        words = page.locator("#words .word.active")
        print("Nuværende ord:", words.inner_text())
        page.keyboard.type(words.inner_text())
        page.keyboard.press("Space")
        time.sleep(0.1)
        if words.count() < 1:
            break

    input("Tryk enter for at lukke siden type beat")

    browser.close()
