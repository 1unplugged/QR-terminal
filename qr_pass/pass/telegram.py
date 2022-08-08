import telegram


TELEGRAM_TOKEN = '5488232009:AAHB47xvC1mHST0cOOKQasasFcH0l7gHjdg'
TELEGRAM_CHAT_ID = '536579143'


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except telegram.TelegramError:
        return False
    return True
