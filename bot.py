from telegram.ext import Updater, CommandHandler
import random
import os

# ======= CONFIG =======
TOKEN = os.environ.get("TOKEN")  # Get your bot token from Render environment variables

# Default settings
pairs = ['EUR/USD', 'GBP/USD', 'USD/CAD', 'USD/JPY', 'EUR/GBP']
time_frame = '5m'
expiration = 5  # minutes

# ======= FUNCTIONS =======
def generate_signal():
    pair = random.choice(pairs)
    action = random.choice(['BUY', 'SELL'])
    return f"{pair} | {action} | Time Frame: {time_frame} | Expiration: {expiration}m"

# Command: /signal → sends one signal
def send_signal(update, context):
    signal = generate_signal()
    update.message.reply_text(signal)

# Command: /settf <timeframe> → set time frame
def set_timeframe(update, context):
    global time_frame
    if context.args:
        time_frame = context.args[0]
        update.message.reply_text(f"Time frame set to {time_frame}")
    else:
        update.message.reply_text("Usage: /settf 1m or 5m or 15m or 1h")

# Command: /setexp <minutes> → set expiration
def set_expiration(update, context):
    global expiration
    if context.args:
        expiration = int(context.args[0])
        update.message.reply_text(f"Expiration set to {expiration} minutes")
    else:
        update.message.reply_text("Usage: /setexp 1 or 5 or 15")

# ======= BOT SETUP =======
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add commands
dispatcher.add_handler(CommandHandler('signal', send_signal))
dispatcher.add_handler(CommandHandler('settf', set_timeframe))
dispatcher.add_handler(CommandHandler('setexp', set_expiration))

# Start the bot
print("Bot is running 24/7. Send /signal in Telegram to get a Forex signal!")
updater.start_polling()
updater.idle()
