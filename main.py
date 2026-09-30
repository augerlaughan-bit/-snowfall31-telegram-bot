
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

    # Boutons et liens corrigés
    keyboard = [
        [
            InlineKeyboardButton(
                text="📱 Ouvrir la mini-app",
                web_app=WebAppInfo(
                    url="https://augerlaughan-bit.github.io/-snowfall31-telegram-bot/"
                )
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Canal",
                url="https://t.me/+Ar5IdGn5wckzYjA0"
            ),
            InlineKeyboardButton(
                text="📞 Contacter",
                url="https://t.me/snnow31"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ Avis clients",
                url="https://t.me/+IvnpxHvvDv85NmI0"
            )
        ],
        [
            InlineKeyboardButton(
                text="📤 Partager le bot",
                url="https://t.me/share/url?url=https%3A%2F%2Ft.me%2Fsnow31_bot&text=Viens%20d%C3%A9couvrir%20ce%20bot%20%F0%9F%91%89"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message de bienvenue
    texte_bienvenue = (
        "Bienvenue sur notre bot snowfall31 👋\n"
        "Vous trouverez ici 👇\n\n"
        "- Image 📸\n"
        "- Menu Mini App 🤖\n"
        "- Lien de Contact ☎️📱\n"
        "- Actu et Promo 🎁"
    )

    # Envoi de la photo et des boutons
    try:
        with open("IMG_0480.jpeg", "rb") as photo_file:
            await update.message.reply_photo(
                photo=photo_file,
                caption=texte_bienvenue,
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        await update.message.reply_text(
            texte_bienvenue,
            reply_markup=reply_markup
        )


def main() -> None:
    # Récupération du token Telegram
    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        logger.error("Aucun token Telegram trouvé.")
        return

    application = ApplicationBuilder().token(token).build()

    # Enregistrement de /start
    application.add_handler(CommandHandler("start", start))

    # Démarrage du bot
    logger.info("Démarrage du bot...")
    application.run_polling()


if __name__ == "__main__":
    main()
