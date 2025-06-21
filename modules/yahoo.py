from playwright.async_api import async_playwright

async def check(email):
    print("[Yahoo]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://login.yahoo.com/forgot")
            await page.fill('input[name="username"]', email)
            await page.click('input#login-signin')
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "Sorry, we don’t recognize" in content:
                print("❌ Not found.")
            elif "Verify your identity" in content or "we've sent a code" in content:
                print("✅ Found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
