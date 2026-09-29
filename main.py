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
    # Création du clavier avec tous les boutons
    keyboard = [
        [InlineKeyboardButton(text="🛍️ Ouvrir la Boutique Snowfall 31", web_app=WebAppInfo(url="https://augerlaughan-bit.github.io/-snowfall31-telegram-bot/"))],
        [InlineKeyboardButton(text="📢 Rejoindre le Canal", url="https://t.me/ton_canal")],
        [InlineKeyboardButton(text="💬 Prise de Contact", url="https://t.me/ton_compte")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message de bienvenue avec les boutons
    await update.message.reply_text(
        "Bienvenue sur le bot de Snowfall 31 !",
        reply_markup=reply_markup
    )

def main() -> None:
    # Récupération automatique du token du bot
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logger.error("Aucun token Telegram trouvé.")
        return

    application = ApplicationBuilder().token(token).build()

    # Enregistrement de la commande /start
    application.add_handler(CommandHandler("start", start))

    # Lancement du bot
    logger.info("Démarrage du bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
