from playwright.async_api import async_playwright

async def check(email):
    print("[Microsoft]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://account.live.com/resetpassword.aspx")
            await page.click("#iProofEmail")
            await page.fill("#iProofEmail", email)
            await page.click("#iNext")
            await page.wait_for_timeout(4000)
            content = await page.content()
            if "account doesn’t exist" in content or "couldn’t find an account" in content:
                print("❌ Not found.")
            elif "verify your identity" in content:
                print("✅ Found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
