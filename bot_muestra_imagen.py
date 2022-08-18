import requests
from bs4 import BeautifulSoup
import telebot

bot_token = 'Your_Bot_token'
bot_chatID = 'Your_chatID'
bot = telebot.TeleBot(bot_token, parse_mode=None)

bot.send_message(chat_id = bot_chatID, text= "ask for anything")


#Toma la palabra que le envies y hace que el metodo funcione mientras m= True
@bot.message_handler(func=lambda m: True)
def echo_all(message):

    word = message.text
    url = 'https://www.google.com/search?q={0}&tbm=isch'.format(word)
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    images = soup.findAll('img')
    lista = []

    for image in images:
        lista.append(image.get('src'))

    bot.send_photo(bot_chatID, lista[3])


bot.infinity_polling()


