import telebot
import time
import random
API_KEY = "5132826516:AAE1wTe9E8W3EQN1852ZEI43NfUOKahbCHY"
bot = telebot.TeleBot(API_KEY)
my_id = 722005465
her_id =  1

@bot.message_handler(commands=['start'])
def send_welcome(message):
  if message.chat.id != my_id :bot.send_message(my_id,message.chat.first_name+"  [@"+message.chat.username+"]: "+message.text);bot.send_message(my_id,message.chat.id)
  bot.reply_to(message,"مرحبا بك، كيف يمكنني مساعدتك ؟\n استخدم /help")

@bot.message_handler(commands=['help'])
def send_help(message):
  if message.chat.id != my_id :bot.send_message(my_id,message.chat.first_name+"  [@"+message.chat.username+"]: "+message.text);bot.send_message(my_id,message.chat.id)
  bot.reply_to(message,"يمكنك استخدام الامر /time \n او استخدم هذه الكلمات: \n هلو ، مرحبا ، هاي ، هلا ، هلو ، hi ، شلونك ، شخبارك . .يمكنك استخدام الامر /time \n او استخدم هذه الكلمات: \n هلو ، مرحبا ، هاي ، هلا ، هلو ، hi ، شلونك ، شخبارك . .")

@bot.message_handler(commands=['time','T'])
def echo(message):
  if message.chat.id != my_id :bot.send_message(722005465,message.chat.first_name+"  [@"+message.chat.username+"]: "+message.text);bot.send_message(my_id,message.chat.id)
  H1 = int(time.strftime("%I")) + 3
  if H1 > 12:
    H2 = H1 - 12
    tt = str(H2) + ":" + str(time.strftime("%M"))
    bot.send_message(message.chat.id, tt)

  else:
    tt = str(H1) + ":" + str(time.strftime("%M"))
    bot.send_message(message.chat.id, tt)


#@bot.message_handler(commands=["mss"])
#def say_S(message):
#  if message.chat.id == my_id:
#    text1 = message.text.split()
#    idx = text1[1]
#    N = message.text.find('&');N+=2
#    bot.send_message(idx,message.text[N:])
#    bot.send_message(message.chat.id,"done")




#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    chat_id = message.text.split()[0]
#    text = ' '.join(message.text.split()[1:])
#    bot.send_message(chat_id, text)


@bot.message_handler(content_types=["text"])
def say_hi(message):
  if message.chat.id !=722005465:
    bot.send_message(722005465,message.chat.first_name+"  [@"+message.chat.username+"]: "+message.text)
    bot.send_message(my_id,message.chat.id)
    inp1 = ["هلو","هلا","هاي","مرحبا","اهلو"]
    for i in range(len(inp1)):
      text = inp1[i]
      if text in message.text :
        say_hi = ["هلو 🤍","اهلا✨","مرحبا✨","😶"]
        EG = say_hi
        I = random.randrange(0,len(EG))
        bot.send_message(message.chat.id,EG[I])

    inp2 = ["hi","hello"]
    for i in range(len(inp2)):
      text = inp2[i]
      if text in message.text.lower() :
        say_Hi = ["Hi 🖤","Hello 🤍","Sup 🫡"]
        EG = say_Hi
        I = random.randrange(0,len(EG), 1)
        bot.send_message(message.chat.id,EG[I])

    inp3 = ["شخبارك","شلونك","sup"]
    for i in range(len(inp3)):
      text = inp3[i]
      if text in message.text.lower() :
        say_fine = ["زين 🖤","بخير 🤍","I am fine and you ? 🫡"]
        EG = say_fine
        I = random.randrange(0,len(EG), 1)
        bot.send_message(message.chat.id,EG[I])
  else:
    text = message.text
    # Extract the chat ID of the original message
    reply_chat_id = message.reply_to_message.text

    # Send a reply to the original message with the chat ID
    bot.send_message(reply_chat_id,text)
    bot.send_message(my_id,"✔.")

print("runing . . .")
bot.polling()