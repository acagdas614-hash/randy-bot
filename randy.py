import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import aiohttp

API_ID = 32146126
API_HASH = "3d51556b7187ea8b556b53a162e8f7d2"
SESSION_STRING = "1BJWap1sBuydw0i7VNUyFC6pLOPEMBnPwfRJ6_nyGA8ga9CcFKtpgiP2nZ-i8fapAukfsrbsy6ubOovXdJyXm8s1mfMG8f9K01JLn-lynPAMwCvELq49Tadqgg7lf-b60EYhz_vIBNqIHL190vTdbSWADJqnIZox_u90e7yavpxDl77BWQ-Gmj8oVhl2pdCrxESwY21Po5sufe6E5_M_xFV-sSC44Peu_dY9eHkRTz-ZzEkSlpe7-eG8el5yG1wOuE0k3Oo7vNH8Aa0if3678HNlOVCRzpTeSTeI8sB9v4jEz_oE8UmzIica9bJoS_Vk7e10YX23ATPvnssWeiWIMbhZVYc83S8g="
GRUP_ID = -1002206221644
BOT_TOKEN = "8743799471:AAFk8DYAJ53tCRlKvm2zPbBJ5YGSlo2peTM"
CHAT_ID = 6409974525

async def bot_bildirim_gonder(session, mesaj):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        async with session.post(url, data={"chat_id": CHAT_ID, "text": mesaj}) as resp:
            pass
    except Exception as e:
        print(f"Hata: {e}")

async def main():
    async with aiohttp.ClientSession() as http_session:
        client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
        await client.start()
        print("✅ Bağlandı, Randy izleniyor...")

        @client.on(events.NewMessage(chats=GRUP_ID))
        async def handler(event):
            sender = await event.get_sender()
            if sender and sender.username and sender.username.lower() == "randymbot":
                mesaj = event.message.message or "(Mesaj yok)"
                await bot_bildirim_gonder(http_session, f"🤖 Randy Bot yazdı!\n\n{mesaj}")
                print("Bildirim gönderildi!")

        await client.run_until_disconnected()

asyncio.run(main())
