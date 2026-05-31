import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# --- ၁။ BOT TOKEN ---
BOT_TOKEN = "8887525878:AAEq54_d9jcJUhuaJ4AWrgMla1U9kKqMMQ4" 

# --- ၂။ မက်ဆေ့ခ်ျများ ပြင်ဆင်ရန်နေရာ ---
def get_welcome_text():
    return (
        "👋 **AERO Gaming Store မှ လှိုက်လှဲစွာ ကြိုဆိုပါတယ်ဗျာ!** 🎮\n\n"
        "အခုအချိန်မှာ Admin အပြင်ရောက်နေလို့ Bot မှ အလိုအလျောက် အကြောင်းပြန်ပေးထားပါတယ်ခင်ဗျာ။\n"
        "မိမိသိရှိလိုသည့် အချက်အလက်များကို အောက်ပါ Keyword များရိုက်၍ မေးမြန်းနိုင်ပါတယ် -\n\n"
        "👉 **kpay** သို့မဟုတ် **wave** - ငွေလွှဲအကောင့်များ သိရန်\n"
        "👉 **time** - အော်ဒါတင်ရမည့် အချိန်နှင့် ဖြည့်ပေးမည့်အချိန် သိရန်\n"
        "👉 **price** သို့မဟုတ် **ဈေး** - Diamond ဈေးနှုန်းများ သိရန်\n"
        "👉 **link** - မင်မင်ရဲ့ Channel နှင့် Group Link များ သိရန်"
    )

def reply_handler(update, context):
    user_text = update.message.text.lower().strip()
    
    # (က) ဝယ်သူက hi / hello / ဟိုင်း လို့ ပို့မှ ပြန်မည့်အပိုင်း
    if user_text in ["hi", "hello", "ဟိုင်း", "hey"]:
        update.message.reply_text(get_welcome_text(), parse_mode="Markdown")

    # (ခ) KPay / WavePay ပုံစံ
    elif "kpay" in user_text or "wave" in user_text or "pay" in user_text:
        msg = (
            "💳 **Payment Accounts**\n\n"
            "* KPay: `09799747004`\n"
            "* WavePay: `09799747004`\n\n"
            "*(Account Name: Khant Min Hein)*\n\n"
            "⚠️ *အရေးကြီးချက်:* ငွေလွှဲပြီးပါက ပြေစာ (Screenshot) ကို Group ထဲသို့ တိကျစွာ ပို့ပေးပါရန်။"
        )
        update.message.reply_text(msg, parse_mode="Markdown")

    # (ဂ) အော်ဒါတင်ချိန် / ဖြည့်ချိန်
    elif "time" in user_text or "အချိန်" in user_text or "order" in user_text:
        msg = (
            "⏳ **Order Time Schedule**\n\n"
            "✅ **အော်ဒါတင်ခြင်း:** ဝယ်ယူလိုသူများအနေဖြင့် အော်ဒါများကို **၂၄ နာရီပတ်လုံး အချိန်မရွေး** တင်ထားနိုင်ပါသည်။\n"
            "⏰ **အော်ဒါဖြည့်ခြင်း:** တင်ထားသော အော်ဒါများကို **ညနေ ၆ နာရီမှ ၁၀ နာရီအတွင်း** အစဉ်လိုက် ဖြည့်ပေးသွားမည်ဖြစ်ပါသည်။"
        )
        update.message.reply_text(msg, parse_mode="Markdown")

    # (ဃ) ဈေးနှုန်းမေးမြန်းခြင်း
    elif "price" in user_text or "ဈေး" in user_text:
        msg = (
            "💰 **Diamond ဈေးနှုန်းများ သိရှိရန်**\n\n"
            "ယနေ့ Diamond ဈေးနှုန်းများကို မင်မင်ရဲ့ **Official Group** ၏ ထိပ်ဆုံးရှိ **Pinned Message** 📌 တွင် အမြဲတမ်း Update ပြုလုပ်ပေးထားပါသည်ခင်ဗျာ။\n\n"
            "ဈေးနှုန်းများကို အောက်ပါ Link မှတစ်ဆင့် ဝင်ရောက်ကြည့်ရှုနိုင်ပါသည် -\n"
            "👉 [AERO Gaming Group Pinned Message](https://t.me/aerogamingstoregp21/1)"
        )
        update.message.reply_text(msg, parse_mode="Markdown", disable_web_page_preview=False)

    # (င) Channel / Group Links
    elif "link" in user_text or "လင့်" in user_text or "join" in user_text:
        keyboard = [
            [InlineKeyboardButton("📢 Join Our Channel", url="https://t.me/Aerogamingstore21")],
            [InlineKeyboardButton("💬 Join Our Group", url="https://t.me/aerogamingstoregp21")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "🔗 **AERO Gaming Store ရဲ့ Official Links များ**\n\nChannel ကို Join ထားပြီး Group ထဲမှာ အော်ဒါတင်နိုင်ပါတယ်ဗျာ -", 
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    # (စ) Keyword မဟုတ်လျှင် ပြန်မဖြေပါ
    else:
        return

def start_command(update, context):
    update.message.reply_text(get_welcome_text(), parse_mode="Markdown")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_handler))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

