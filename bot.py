import telebot
import psycopg2

bot = telebot.TeleBot("1081872084:AAG5qlR0IoLM4wXJhAdnQ98YYz-ubQMT-bw")

user_data ={}

con = psycopg2.connect(
    host = "localhost",
    database = "restaurants",
    user = "postgres",
    password = "2825767Yer",
    port = "5432"
)

# cur = con.cursor()
# cur.execute("select restourant_name from restourants")
# rows = cur.fetchall() 


class User:
    def __init__(self, restourant_name):
        self.restourant_name = restourant_name

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
        msg = bot.send_message(message.chat.id,"Я бот поисковик какой ресторан вы ищите?")
        bot.register_next_step_handler(msg,process_search_step)

def process_search_step(message):
    try:
        user_id =  message.from_user.id
        user_data[user_id] = User(message.text)
        msg = message.text
        sql = "select * from restaurants_almaty where restaurant_name = '"+msg+"'"
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall() 
        if len(rows) == 0:
            bot.reply_to(message, "У нас нету такого ресторана")
        for j in rows:
            if j[0] in msg:
                bot.send_message(message.chat.id,str('Имя ресторана: ')+j[0])
                bot.send_message(message.chat.id,str('Адрес: ')+j[1])
                bot.send_message(message.chat.id,str('Кухни: ')+j[3])
                bot.send_message(message.chat.id,str('Контакты: ')+j[2])
                bot.send_message(message.chat.id,str('Средняя цена: ')+j[4])
                bot.send_message(message.chat.id,str('Дополнительные услуги: ')+j[5])
                break
                
    except Exception as e:
        bot.reply_to(message, "Вы ввели что-то некоректно повторите попытку")


@bot.message_handler(commands=["location"])
def geo(message, *args, **kwargs):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение",request_location=True)
    keyboard.row(button_geo)
    bot.send_message(message.chat.id, "Нажмите на кнопку и передайте мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))


bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()
if __name__ == '__main__':
    bot.polling(none_stop=True)
cur.close()
con.close()




#new code for bot


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

# cur = con.cursor()
# cur.execute("select restourant_name from restourants")
# rows = cur.fetchall() 




#Database 





class User:
    def __init__(self, restourant_name):
        self.restourant_name = restourant_name

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
        msg = bot.send_message(message.chat.id,"Я бот поисковик ресторанов, какой ресторан ищите")
        bot.register_next_step_handler(msg,process_search_step)


userLat=0
userLon=0
@bot.message_handler(commands=["location"])
def geo(message, *args, **kwargs):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение",request_location=True)
    keyboard.row(button_geo)
    bot.send_message(message.chat.id, "Нажмите на кнопку и передайте мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])


def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
    # return [message.location.latitude,message.location.longitude]
        userLat = message.location.latitude
        userLon= message.location.longitude


# print('here')
# print(location())

def process_search_step(message):

    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = message.text
        #if message.location is not None:
        # r = 6371.0090667
        # lat1 = lat1 * math.pi / 180.0
        # long1 = long1 * math.pi / 180.0
        # lat2 = lat2 * math.pi / 180.0
        # long2 = long2 * math.pi / 180.0
        # dlon = long1 - long2
        # d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(dlon)) * r
        # if d < 50:
        # if message.location is not None:
        #     userX = message.location.latitude
        #     userY = message.location.longitude
        sql = "select * from restaurant_boss where city = '"+msg+"'"
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        if len(rows) == 0:
            bot.reply_to(message, "У нас нету такого ресторана")

        for j in rows:
            if message.location is not None:
                if msg in j[0]:
                    lat,lon = location(message)
                    bot.send_message(message.chat.id,str("Latitude: ") + j[
                                           7] + "\n\n" + str("Longitude: ") + j[8])
                    
        # for j in rows:
        #     if msg in j[0]:
        #         lat,lon = location(message)
        #         bot.send_message(message.chat.id,str("Latitude: ") + j[
        #                                    7] + "\n\n" + str("Longitude: ") + j[8])
    except Exception as e:
        bot.reply_to(message, "Вы ввели что-то некоректно повторите попытку")






# @bot.message_handler(commands=["geo"])
# def geo_send(message):
#     bot.send_location(message.chat.id, 42.3628991,69.6320613)

bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling(none_stop=False)



con.close()
