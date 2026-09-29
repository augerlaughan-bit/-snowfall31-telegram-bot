# SNOWFALL31 — Bot Telegram de commandes

Bot Telegram prêt à personnaliser pour :
- 🛒 prise de commande
- 🚚 livraison
- 🤝 meet up
- 📦 suivi des commandes
- 🔔 notification automatique du client
- 👑 commandes admin
- 🟢/🔴 état de la boutique

## 1. Créer le bot Telegram

Dans Telegram, ouvre **@BotFather** puis :
1. `/newbot`
2. Donne un nom au bot.
3. Donne un username qui termine par `bot`.
4. Copie le token fourni.

Ne partage jamais ce token publiquement.

## 2. Trouver ton ID Telegram

Tu peux utiliser un bot de type **@userinfobot** pour obtenir ton identifiant Telegram.

## 3. Configuration

Copie `.env.example` vers `.env` et remplis :

```env
BOT_TOKEN=ton_token
SHOP_NAME=SNOWFALL31
ADMIN_IDS=ton_id_telegram
DB_PATH=orders.db
```

Pour plusieurs admins :

```env
ADMIN_IDS=123456789,987654321
```

## 4. Installation locale

Python 3.12 recommandé.

```bash
python -m venv .venv
```

Windows :
```bash
.venv\Scripts\activate
```

Linux/macOS :
```bash
source .venv/bin/activate
```

Puis :

```bash
pip install -r requirements.txt
python -m bot.main
```

## 5. Commandes admin

- `/orders` — voir les dernières commandes
- `/open` — message d'ouverture
- `/close` — message de fermeture

Quand une commande arrive, l'admin reçoit des boutons pour :
- ✅ Acceptée
- 🛵 Livraison en cours
- 🤝 Meet up disponible
- ❌ Annulée

Le client reçoit automatiquement la mise à jour.

## 6. Mise en ligne

Le plus simple est de louer un petit serveur Linux/VPS, installer Docker puis :

```bash
docker compose up -d --build
```

Le dossier `data/` conserve la base SQLite.

## À personnaliser ensuite

- catalogue avec prix et photos
- bouton « Commander » par produit
- horaires réels
- zone de livraison
- frais de livraison
- paiement en ligne
- code promo
- statistiques
- panneau admin web
- messages automatiques
- intégration d'un logo SNOWFALL31
