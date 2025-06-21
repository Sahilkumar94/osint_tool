from playwright.async_api import async_playwright

async def check(email):
    print("[Instagram]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://www.instagram.com/accounts/password/reset/")
            await page.fill('input[name="cppEmailOrUsername"]', email)
            await page.click('button[type="submit"]')
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "We sent an email" in content:
                print("✅ Found.")
            elif "No users found" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
