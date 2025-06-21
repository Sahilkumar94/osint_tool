import asyncio
from modules import facebook, instagram, google, microsoft, snapchat, twitter, yahoo, amazon, flipkart

async def main(email):
    print(f"\n🔍 Checking OSINT email linkage for: {email}\n")
    await facebook.check(email)
    await instagram.check(email)
    await google.check(email)
    await microsoft.check(email)
    await snapchat.check(email)
    await twitter.check(email)
    await yahoo.check(email)
    await amazon.check(email)
    await flipkart.check(email)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_email_all.py <email>")
    else:
        asyncio.run(main(sys.argv[1]))
