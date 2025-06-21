from playwright.async_api import async_playwright

async def check(email):
    print("[Twitter]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://twitter.com/i/flow/signup")
            await page.click("text=Use email instead")
            await page.fill('input[name="email"]', email)
            await page.wait_for_timeout(3000)
            content = await page.content()
            if "email has already been taken" in content.lower():
                print("✅ Found.")
            elif "enter your email" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
