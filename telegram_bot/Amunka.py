import telebot
from telebot import types

API_TOKEN = "6191606700:AAGKoMcJIo8AbIAeCaTOnEkpPHuCHBEQmpo"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    photo = open("exotic_fruits.png", "rb")
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id,
                     text="<b>Welcome! You can order at our shop for the best Exotic Fruits. Please "
                          "use the command /order to make an order.</b>",
                     parse_mode="html")


@bot.message_handler(commands=["order"])
def Order(message):
    markup = types.ReplyKeyboardMarkup()
    order = types.KeyboardButton("Order")
    address = types.KeyboardButton("My address")
    markup.add(address, order)
    bot.send_message(message.chat.id,
                     "Please send your address by using the button My address and choose an order by using the button Order.",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hi! If you want to make an order, please tap /order", parse_mode="html")
    elif message.text == "Order":
        markup = types.ReplyKeyboardMarkup()
        fruit_package_small = types.KeyboardButton("Small fruit package")
        fruit_package_medium = types.KeyboardButton("Medium fruit package")
        fruit_package_large = types.KeyboardButton("Large fruit package")
        markup.add(fruit_package_small, fruit_package_medium, fruit_package_large)
        bot.send_message(message.chat.id, "Please choose the size of the fruit package you want to buy",
                         reply_markup=markup)
    elif message.text == "Small fruit package":
        bot.send_message(message.chat.id,
                         "Great! Small fruit package costs 15$. Send 50% prepayment to Kaspi - +77015065759. Send "
                         "Done when you pay the half of the cost!",
                         parse_mode="html")
    elif message.text == "Medium fruit package":
        bot.send_message(message.chat.id,
                         "Great! Medium fruit package costs 25$. Send 50% prepayment to Kaspi - +77015065759. Send Done"
                         "when you pay the half of the cost!",
                         parse_mode="html")
    elif message.text == "Large fruit package":
        bot.send_message(message.chat.id,
                         "Great! Large fruit package costs 35$. Send 50% prepayment to Kaspi - +77015065759. Send Done "
                         "when you pay the half of the cost!",
                         parse_mode="html")
    elif message.text == "My address":
        bot.send_message(message.chat.id,
                         "Please, call this number +77015065759 and send your address - it can be unsafe to send it "
                         "here.",
                         parse_mode="html")
    elif message.text == "Done":
        video = open("exotic_fruits.mp4", "rb")
        bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, "Thank you for your order!", parse_mode="html")
        voice = open("thanks.mp3", "rb")
        bot.send_audio(message.chat.id, voice)
    else:
        bot.send_message(message.chat.id, "Hi! If you want to make an order, please tap /order", parse_mode="html")


@bot.message_handler(content_types=["photo", "audio"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Okay!", parse_mode="html")


def get_user_audio(message):
    bot.send_message(message.chat.id, "Okay!", parse_mode="html")


bot.polling(none_stop=True)
