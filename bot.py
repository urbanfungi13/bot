from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8397591047:AAF84CGi_QdE4fcRIY7O-mwVkBe0xQWleKs"

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌍 Site Web", url="https://example.com")],
        [InlineKeyboardButton("📸 Instagram", url="https://instagram.com/toncompte")],
        [InlineKeyboardButton("🛒 Boutique", url="https://tonsite.com/shop")],
        [InlineKeyboardButton("📧 Contact", url="mailto:contact@tonsite.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenue 👋 Choisis un lien :", reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot lancé")
    app.run_polling()

if __name__ == "__main__":
    main()
