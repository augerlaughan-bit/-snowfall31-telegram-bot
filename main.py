import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Récupération du token configuré dans tes variables d'environnement Railway
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  # 1. L'image de présentation (tu peux remplacer le lien par l'URL de ton image)
  photo_url = "IMG_0347.PNG"  # Exemple d'image

  # 2. Le texte de bienvenue
  caption = (
      "Bienvenue sur notre bot 👋\n"
      "Vous trouverez ici 👇\n"
      "- Image 📸\n"
      "- Menu Mini App 🤖\n"
      "- Lien de Contact ☎️📲\n"
      "- Actu et Promo 🎁"
  )

  # 3. Les boutons interactifs (Inline Keyboards)
  keyboard = [
      [InlineKeyboardButton("📱 Ouvrir la mini-app", url="https://ton-lien.com")],
      [
          InlineKeyboardButton("💬 Canal", url="https://t.me/ton_canal"),
          InlineKeyboardButton("📞 Contacter", url="https://t.me/ton_pseudo"),
      ],
      [
          InlineKeyboardButton(
              "🔵 Contact Signal", url="https://signal.me/#..."
          )
      ],
      [
          InlineKeyboardButton(
              "🛍️📸 Avis / Retour", url="https://t.me/ton_lien_avis"
          )
      ],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)

  # Envoi de la photo avec le texte et les boutons
  await update.message.reply_photo(
      photo=photo_url, caption=caption, reply_markup=reply_markup
  )


def main():
  application = ApplicationBuilder().token(TOKEN).build()
  application.add_handler(CommandHandler("start", start))

  print("Le bot est démarré...")
  application.run_polling()


if __name__ == "__main__":
  main()
