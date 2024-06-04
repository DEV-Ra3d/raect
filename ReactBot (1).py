#by @Se7en_Eyes & @F_E_Y
import telebot
import requests
import json, random

API_TOKEN = '6742371774:AAGFfOZu-ZqE1HVHGW4snezNft5XspNBCbs'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def start(message):
    reactions = ["👍", "❤️", "🔥", "🥰", "👏", "😁"]
    emoji = random.choice(reactions)
    response = send_message_react(
        {
            'chat_id': message.chat.id,
            'message_id': message.message_id,
            'reaction': json.dumps([{'type': "emoji", "emoji": emoji}])
        }
    )

def send_message_react(datas={}):
    url = "https://api.telegram.org/bot" + API_TOKEN + "/" + 'setmessagereaction'
    response = requests.post(url, data=datas)

    if response.status_code != 200:
        return "Error: " + response.text
    else:
        return response.json()

bot.infinity_polling()