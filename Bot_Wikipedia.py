import telebot, wikipedia, re
bot = telebot.TeleBot('7220117180:AAHsQ-bNT1ZtwbLb2z6SUiLjpahzmCfvwI8')
wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext1 = ny.content[:1000]
        wikimass = wikitext1.split('.')
        wikimass = wikimass[:-1]
        wikitext2 = ''
        for x in wikimass:
            if not ('==' in x):
                if len((x.strip())) > 3:
                   wikitext2 = wikitext2+x+'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception:
        return 'В Wikipedia нет об этом информации'
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Напишите мне любое слово, и я найду его значение на Wikipedia')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
bot.polling(none_stop=True, interval=0)