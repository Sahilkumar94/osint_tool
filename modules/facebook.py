from playwright.async_api import async_playwright

async def check(email):
    print("[Facebook]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://www.facebook.com/login/identify")
            await page.fill('input[name="email"]', email)
            await page.click('button[type="submit"]')
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "No search results" in content:
                print("❌ Not found.")
            elif "profile" in content or "We've sent" in content:
                print("✅ Found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
