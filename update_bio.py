from playwright.async_api import async_playwright
import os

SESSION_DIR = "sessions"

async def update_tiktok_bio(new_bio):
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", headless=False)
        context = await browser.new_context(storage_state=f"{SESSION_DIR}/state.json" if os.path.exists(f"{SESSION_DIR}/state.json") else None)
        page = await context.new_page()

        if not os.path.exists(f"{SESSION_DIR}/state.json"):
            await page.goto("https://www.tiktok.com/login")
            print("Silakan login secara manual di browser. Tekan Enter setelah login.")
            input("Tekan Enter jika sudah login...")
            os.makedirs(SESSION_DIR, exist_ok=True)
            await context.storage_state(path=f"{SESSION_DIR}/state.json")
        
        await page.goto("https://www.tiktok.com/settings/profile")
        await page.wait_for_selector("textarea")
        await page.fill("textarea", new_bio)
        await page.click("button:has-text('Save')")
        await page.wait_for_timeout(2000)
        await browser.close()
