import telebot
from telegram.client import Telegram

tg = Telegram(
    api_id='223471',
    api_hash='35e5fd598146bd69a2225b5402ab706c',
    phone='+79273235411',
    database_encryption_key='changeme1234',
)
tg.login()


def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    # we need this because of different message types: photos, files, etc.
    message_text = message_content.get('text', '').lower()

    if message_text == 'ping':
        chat_id = update['message']['chat_id']
        print(f'Ping has been received from {chat_id}')
        tg.send_message(
            chat_id=chat_id,
            text='pong',
        )

tg.add_message_handler(new_message_handler)
tg.idle()  # blocking waiting for CTRL+C

class Hero:
    def __init__(self, id, username):
        self.id = id
        self.money = 10
        self.stamina = 5
        self.lvl = 1
        self.name = username
    def ch_money(self, value):
        self.money = self.money+value
    def ch_stamina(self, value):
        self.stamina += value
    def lvl_up(self):
        self.lvl += 1



#---------------------------------------------------------------

players = {}

bot = telebot.TeleBot("560321952:AAGZ6-f8Iey7QzFqhRv2r-CvcASA5quKEGc")

def send_info(message, player):
    bot.send_message(message.from_user.id, player.name + " , money - " + str(player.money))



@bot.message_handler(commands=['startgame'])
def start(message):
    print("Он прислал старт")
    if message.from_user.id in players:
        player = players.get(message.from_user.id)
        send_info(message, player)
    else:
        player = Hero(message.from_user.id, message.from_user.username)
        players[message.from_user.id] = player
        bot.send_message(message.from_user.id, "Приветствую, игрок!")
        send_info(message, player)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("Он прислал текст")
    if message.text == "Hoi":
        bot.send_message(message.chat.id, "boi")

bot.polling()



