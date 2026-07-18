
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import sqlite3

TOKEN = "8866419323:AAGlWfyIbHI9TZB5XjdvYD_KscHFrHS1t2Y"

conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    await update.message.reply_text("✅ Welcome!")

async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cur.execute("SELECT COUNT(*) FROM users")
    total = cur.fetchone()[0]
    await update.message.reply_text(f"👥 Total Users: {total}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("users", users))

print("Bot is running...")
app.run_polling()
