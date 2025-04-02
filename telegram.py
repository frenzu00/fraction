import telebot
from telebot import types

bot = telebot.TeleBot('7751235118:AAEzcuRNmERlN2c0c_HKim0B1_zBDlB0wGM')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, " Привет! Я твой бот-архивариус!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Автоботы')
        btn2 = types.KeyboardButton('Десептиконы')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '❓ Какую фракцию вы выбираете', reply_markup=markup) #ответ бота
    elif message.text == 'Автоботы':
        bot.send_message(message.from_user.id,"прекрасный выбор"+'[ссылке](https://transformers.fandom.com/ru/wiki/Автоботы)', parse_mode='Markdown')
        if message.text == 'Автоботы':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("да")
                btn2 = types.KeyboardButton("нет")
                markup.add(btn1,btn2)
                bot.send_message(message.from_user.id,"согласны ли вы войти в наши ряды", reply_markup=markup)
    elif message.text == 'да':
                bot.send_message(message.from_user.id,"сегодня вы стали новой бетой", parse_mode='Markdown')
    elif message.text == 'нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Автоботы')
        btn2 = types.KeyboardButton('Десептиконы')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id,"удалите чат",reply_markup=markup)
    elif message.text == 'Десептиконы':
        bot.send_message(message.from_user.id,"вы уверены в своём выборе?"+'[ссылке](https://transformersfanon.fandom.com/ru/wiki/Империя_десептиконов)', parse_mode='Markdown')
        if message.text == 'Десептиконы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("да")
            btn2 = types.KeyboardButton("нет")
            markup.add(btn1,btn2)
            bot.send_message(message.from_user.id,"согласны ли вы войти в наши ряды", reply_markup=markup)
    elif message.text == 'да':
        bot.send_message(message.from_user.id,"сегодня вы стали новой бетой", parse_mode='Markdown')
    elif message.text == 'нет':
        bot.send_message(message.from_user.id,"удалите чат", parse_mode='Markdown')
    if message.text == 'да':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("конечно!")
                btn2 = types.KeyboardButton("не знаю")
                markup.add(btn1,btn2)
                bot.send_message(message.from_user.id,"знаете ли вы историю войны трансформеров?", reply_markup=markup)
    elif message.text == 'конечно!':
        bot.send_message(message.from_user.id,"замечательно,если хотите можете прочитать легенду об Олслпарке"+'[ссылке](https://com-x.life/10973-transformerssaga-of-the-allspark-transformerysaga-ob-ollsparke.html)', parse_mode='Markdown')
    elif message.text == 'не знаю':
        bot.send_message(message.from_user.id,"всё ещё в переди!"+"[ссылке](https://transformersfanon.fandom.com/ru/wiki/Первая_Кибертронская_война)", parse_mode='Markdown')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("и тебе")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "удачи", reply_markup=markup)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть