import telebot

token = '2107570428:AAFuZkFAmRk9IFz0UkNdy1DQvqkIZ42-k2I'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Отлично', 'Плохо')
    bot.send_message(message.chat.id, 'Привет!Как дела?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, 'Это очень хорошо!')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Я очень рад!')


bot.polling()
