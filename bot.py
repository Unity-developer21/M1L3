import telebot

bot = telebot.TeleBot('8371716926:AAHntDy2QgUlKdzxGD-KZR83BR_-j2lNEKw')
ban_words = ['дурак', 'блин', 'http']

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
@bot.message_handler(func=lambda message: True)
def ban(message):
    user_message = message.text
    for word in ban_words:
        if word in user_message:
            bot.ban_chat_member(message.chat.id,
                                 message.from_user.id)
            bot.send_message(message.chat.id,
                f'забанен пользоваель {message.
                                       from_user.first_name}')
            return
bot.infinity_polling()
