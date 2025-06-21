from playwright.async_api import async_playwright

async def check(email):
    print("[Google]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://accounts.google.com/signin/v2/usernamerecovery")
            await page.fill('input[type="email"]', email)
            await page.click('button[type="submit"]')
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "We found your Google Account" in content:
                print("✅ Found.")
            elif "Couldn't find your Google Account" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
