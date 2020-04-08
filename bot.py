import telebot
import psycopg2
import math
bot = telebot.TeleBot("1081872084:AAG5qlR0IoLM4wXJhAdnQ98YYz-ubQMT-bw")

user_data ={}

con = psycopg2.connect(
    host = "localhost",
    database = "restaurants",
    user = "postgres",
    password = "2825767Yer",
    port = "5432"
)


class User:
    def __init__(self, restourant_name):
        self.restourant_name = restourant_name

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
        msg = bot.send_message(message.chat.id,"Я бот поисковик ресторанов, где вы ищите ресторан")
        bot.register_next_step_handler(msg,process_geo_step)


# @bot.message_handler(commands=["location"])
# @bot.message_handler(content_types=["location"])
# def process_hello_step(message):
#     try:
#         user_id = message.from_user.id
#         user_data[user_id] = User(message.text)
#
#         msg = bot.send_message(message.chat.id,"Отправьте свое местоположение")
#         bot.register_next_step_handler(msg,process_geo_step)
#     except Exception as e:
#         bot.reply_to(message,"Ooops")
@bot.message_handler(content_types=["location"])
def process_geo_step(message):
    try:
        global user_message
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.row(button_geo)
        msg = bot.send_message(message.chat.id, "Отправьте свое местоположение", reply_markup=keyboard)
        # if message.location is not None:
        #     print(message.location)
        #     print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        bot.register_next_step_handler(msg,process_wait_step)
        user_message = message.text
    except Exception as e:
        bot.reply_to(message, "Ooops")


def process_wait_step(message):
    bot.send_message(message.chat.id, "Пожалуйста ожидайте несколько секунд")
    print(message.location.latitude)
    print(user_message)



# @bot.message_handler(commands=["geo"])
# def geo_send(message):
#     bot.send_location(message.chat.id, 42.3628991,69.6320613)

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling(none_stop=True)



con.close()
