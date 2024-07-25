import wikipedia, re
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
api = '7220117180:AAHsQ-bNT1ZtwbLb2z6SUiLjpahzmCfvwI8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
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
@dp.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id, 'Напишите мне любое слово, и я найду его значение на Wikipedia')
@dp.message_handler(content_types=["text"])
async def handle_text(message):
   await bot.send_message(message.chat.id, getwiki(message.text))
executor.start_polling(dp, skip_updates=True)