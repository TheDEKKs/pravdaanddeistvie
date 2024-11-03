import telebot
from telebot import types
from numpy import*
import time
from time import sleep

bot = telebot.TeleBot('')
player = []


@bot.message_handler(commands=['start'])
def starts(message):
    bot.send_message(message.chat.id, text='Приветствую тебя в боте для игры в правда или действие! Добавь его в бота что бы начать играть. \nЕсли возникнут тех. проблемы пишите @thedekk_me')


@bot.message_handler(commands=['go', 'начать'])
def goplay(message):
    buts = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text='Продолжить', callback_data='gose')
    buts.add(but1)
    bot.send_message(message.chat.id, text="Напишите команду /player и напишите кто будет играть! \n  Если вы готовы играть нажимайте на кнопку:", reply_markup=buts)
    


@bot.message_handler(commands=['player', 'игроки'])
def pl1(message):
    mesg = bot.send_message(message.chat.id, text='Напишите игрока и поставть пробел, после этого отправьте команду ещё раз и повторите дейсвтие. После внесения всех игроков в список можете прописать команду /go : ')
    bot.register_next_step_handler(mesg,player1)


def player1(message):
   text = message.text
   player.append(text)
   print(player)



    


@bot.callback_query_handler(func=lambda callback: callback.data)
def qer(callback):
    if callback.data == 'gose':
        plays = "Сейчас играют: " + ", ".join(player) 
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=plays)
        print(plays)
        bot.send_message(callback.message.chat.id, text="Игра началась! Что бы выбрать рандомных людей пропишите команду /game")

def randomiser_player_one():
    global r_player_one 
    r_player_one = random.choice(player)
    print(r_player_one)

def randomiser_player_two():
    global r_player_two
    
    r_player_two = random.choice(player)
    print(r_player_two)
    if r_player_one == r_player_two:
        randomiser_player_two()
        
        
    else:
        global texts 
        texts = r_player_two + " спрашивает: " + r_player_one + " правда или действие?"

        
        return texts
        


@bot.message_handler(commands=['game'])
def pl1(message):
     bot.send_message(message.chat.id, text="Выбираем игроков...")
     randomiser_player_one()
     randomiser_player_two()
     time.sleep(1)
     if r_player_one == r_player_two or r_player_two == r_player_one:
        randomiser_player_two()
     else:
         texts = r_player_two + " спрашивает: " + r_player_one + " правда или действие?"
         bot.send_message(message.chat.id, text="Игроки выбраны!")
         bot.send_message(message.chat.id, text=texts)
     
     




bot.infinity_polling()