from playwright.async_api import async_playwright

async def check(email):
    print("[Amazon]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://www.amazon.in/ap/forgotpassword?openid.pape.max_auth_age=900&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
            await page.fill('input[id="ap_email"]', email)
            await page.click('input[id="continue"]')
            await page.wait_for_timeout(4000)
            content = await page.content()

            if "we have sent the code" in content:
                print("✅ Found.")
            elif "Wrong or Invalid email address or mobile phone number" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
