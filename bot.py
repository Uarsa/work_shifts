import telebot
from datetime import datetime


bot = telebot.TeleBot("1292084246:AAHOLimjTFKaEajErlOmDUPDETRHiianBXg")


day_of_week = {
        "Monday": "понедельник",
        "Tuesday": "вторник",
        "Wednesday": "среда",
        "Thursday": "четверг",
        "Friday": "пятница",
        "Saturday": "суббота",
        "Sunday": "воскресенье"
    }
    
current_month = int(datetime.now().strftime('%m'))
current_year = int(datetime.now().strftime('%Y'))


def spliter(string):
    
    month = current_month
    year = current_year
    
    s = string.split(" ")
    
    if len(s) == 1:
        day = int(s[0])
    elif len(s) == 2:
        day = int(s[0])
        month = int(s[1])
    else:
        day = int(s[0])
        month = int(s[1])
        year = int(s[2])
        
    
    return w_day(day, month, year)


def w_day(day, month=current_month, year=current_year):
    w = int(datetime(year=2020, month=12, day=15).strftime("%V"))
    d = datetime(year, month, day).strftime("%A")
    
    if w % 3 == 0:
        shift = "вечерняя"
    else:
        shift = "утренняя"
    
    return "{}, {} смена".format(day_of_week[d], shift)


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Привет!/nПришли дату в формате дд мм гг./nЛибо без месяца и/или года, в таком случае они будут текущими.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
                response = spliter(str(message.text))
                bot.send_message(message.chat.id, response)    
        except:
                bot.send_message(message.chat.id, "ОШИБКА...")
             
        
bot.polling(none_stop=True, interval=0)    
