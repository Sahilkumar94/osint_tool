from playwright.async_api import async_playwright

async def check(email):
    print("[Snapchat]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://accounts.snapchat.com/accounts/forgot_password")
            await page.fill('input[name="email"]', email)
            await page.click('button[type="submit"]')
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "email has been sent" in content:
                print("✅ Found.")
            elif "invalid email address" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
