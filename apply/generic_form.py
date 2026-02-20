from playwright.sync_api import sync_playwright


def apply_generic(job):

    print("Generic apply:", job["url"])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(job["url"])

        print("Manual intervention may be needed")

        browser.close()

    return False