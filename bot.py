import telebot
from datetime import datetime


bot = telebot.TeleBot("1292084246:AAHOLimjTFKaEajErlOmDUPDETRHiianBXg")


month_name = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
    }

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


def w_day(day, month, year):
    week = int(datetime(year, month, day).strftime("%V"))
    d = datetime(year, month, day).strftime("%A")
    
    if week % 3 == 0:
        shift = "вечерняя смена\n(14:30 - 23:00)"
    else:
        shift = "утренняя смена\n(7:00 - 15:30)"
        
    if d == "Saturday":
        shift = "выходной"
    elif d == "Sunday":
        shift = "выходной"
    
    return "{} {} {}\n{}, {}".format(day, month_name[month], year, day_of_week[d], shift)


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Пришли дату в формате:\nЧИСЛО МЕСЯЦ ГОД\nЛибо без месяца и/или года, в таком случае они будут текущими.\nПримеры:\n3\n5 8\n10 12 2021", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
                response = spliter(str(message.text))
                bot.send_message(message.chat.id, response)    
        except:
                bot.send_message(message.chat.id, "Неверный формат даты.\nПримеры:\n3\n5 8\n10 12 2021")
             
        
bot.polling(none_stop=True, interval=0)    
