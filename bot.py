import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Le token est stocké dans les variables Railway
TOKEN = os.getenv("TOKEN")

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
    if not TOKEN:
        print("❌ ERREUR : TOKEN manquant. Ajoute la variable TOKEN dans Railway.")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot lancé sur Railway")
    app.run_polling()

if __name__ == "__main__":
    main()