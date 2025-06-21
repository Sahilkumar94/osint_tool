from playwright.async_api import async_playwright

async def check(email):
    print("[Flipkart]")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto("https://www.flipkart.com/account/login")
            await page.fill('input[class="r4vIwl BV+Dqf"]', email)
            await page.click('button[class="QqFHMw twnTnD _7Pd1Fp"]')
            await page.wait_for_timeout(4000)
            content = await page.content()

            # print(content)

            if "Please enter the OTP sent to" in content:
                print("✅ Found.")
            elif "You are not registered with us" in content:
                print("❌ Not found.")
            else:
                print("⚠️ Indeterminate.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            await browser.close()
