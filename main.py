import asyncio
from telethon import TelegramClient, events

# --- အစ်ကို့ရဲ့ API Data များ ---
api_id = 32505104
api_hash = 'de1c0a908f2c18ee6532c900ec48f615'

client = TelegramClient('aero_session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:
        text = event.raw_text.lower()
        
        # --- ကြိုဆိုစကား ---
        if any(x in text for x in ["hi", "hello", "ဟိုင်း", "start"]):
            await event.respond(
                "👋 **AERO Gaming Store မှ လှိုက်လှဲစွာ ကြိုဆိုပါတယ်ဗျာ!** 🎮\n\n"
                "Admin အပြင်ရောက်နေလို့ Bot မှ အလိုအလျောက် အကြောင်းပြန်ပေးထားပါတယ်ခင်ဗျာ။\n\n"
                "👉 **pay** - ငွေလွှဲအကောင့်များ\n"
                "👉 **time** - အော်ဒါတင်ခြင်းနှင့် ဖြည့်ပေးမည့်အချိန်\n"
                "👉 **price** - Diamond ဈေးနှုန်းများ\n"
                "👉 **link** - Channel/Group Link များ"
            )
            
        # --- Pay အကြောင်း ---
        elif "pay" in text or "kpay" in text:
            await event.respond("💳 **Payment:** 09799747004 (Khant Min Hein)\nငွေလွှဲပြီးလျှင် ပြေစာ ပို့ပေးပါရန်။")

        # --- အော်ဒါတင်ခြင်းနှင့် အချိန်အကြောင်း ---
        elif "time" in text or "အချိန်" in text:
            await event.respond(
                "⏳ **Order Time Schedule**\n\n"
                "✅ **အော်ဒါတင်ခြင်း:** ဝယ်ယူလိုသူများအနေဖြင့် အော်ဒါများကို **၂၄ နာရီပတ်လုံး** အချိန်မရွေး တင်ထားနိုင်ပါသည်။\n"
                "⏰ **အော်ဒါဖြည့်ခြင်း:** တင်ထားသော အော်ဒါများကို **ညနေ ၆ နာရီမှ ၁၀ နာရီအတွင်း** အစဉ်လိုက် ဖြည့်ပေးသွားပါမည်။"
            )

        # --- ဈေးနှုန်းအကြောင်း ---
        elif "price" in text or "ဈေး" in text:
            await event.respond("💰 **ဈေးနှုန်းများ:** Group Pinned Message 📌 တွင် ကြည့်ရှုနိုင်ပါသည်။")

        # --- လင့်များ ---
        elif "link" in text:
            await event.respond("🔗 **Channel:** https://t.me/Aerogamingstore21\n💬 **Group:** https://t.me/aerogamingstoregp21")

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
