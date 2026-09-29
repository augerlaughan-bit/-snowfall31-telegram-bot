import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuration des logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Fonction de démarrage /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Organisation des boutons en plusieurs lignes comme sur ton modèle
    keyboard = [
        [InlineKeyboardButton(text="📱 Ouvrir la mini-app", web_app=WebAppInfo(url="https://augerlaughan-bit.github.io/-snowfall31-telegram-bot/"))],
        [
            InlineKeyboardButton(text="💬 Canal", url="https://t.me/ton_canal"),
            InlineKeyboardButton(text="📞 Contacter", url="https://t.me/ton_compte")
        ],
        [InlineKeyboardButton(text="🔵 Contact Signal", url="https://signal.me/#...")],
        [InlineKeyboardButton(text="🛍️📸 Avis / Retour", url="https://t.me/ton_canal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Texte de bienvenue structuré avec des emojis
    texte_bienvenue = (
        "Bienvenue sur notre bot 👋\n"
        "Vous trouverez ici 👇\n\n"
        "- Image 📸\n"
        "- Menu Mini App 🤖\n"
        "- Lien de Contact ☎️📱\n"
        "- Actu et Promo 🎁"
    )

    # Envoi de la nouvelle image IMG_0480.jpeg avec le texte et les boutons
    with open("IMG_0480.jpeg", "rb") as photo_file:
        await update.message.reply_photo(
            photo=photo_file,
            caption=texte_bienvenue,
            reply_markup=reply_markup
        )

def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logger.error("Aucun token Telegram trouvé.")
        return

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("Démarrage du bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
