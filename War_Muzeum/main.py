import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import json


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

TOKEN = '5304372016:AAENuBc5_RPtZdgynzMLz-1J_C5cp_BGQ48'


def start(update, context):
    update.message.reply_text(
        'Здравствуйте! Я, бот помощник сайта "Онлайн-музей реликвий оставшихся с Великой Отечественной войны"! Здесь, вы можете ' 
        "добавить статью о вашей семейной реликвии. Для добавления, пропишите команду /add."
        "Для помощи, пропишпте команду /help.")
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("help", help))


def add(update, context):
    update.message.reply_text(
        "Для добавления статьи, надо написать серию команд:\n 1. /title название статьи \n 2. /text текст статьи \n "
        "3. /image и в следующем сообщении отправить картинку \n 4. /done чтобы закончить статью")
    dp.add_handler(CommandHandler("title", title))
    dp.add_handler(CommandHandler("text", text))
    dp.add_handler(CommandHandler("done", done))
    dp.add_handler(CommandHandler("image", image))


def title(update, context):
    with open('data.json') as file:
        global data
        data = json.load(file)
    file.close()
    point = str(int(str(data.keys()).split("'")[-2]) + 1)
    data[point] = {}
    data[str(data.keys()).split("'")[-2]]['title'] = update.message.text.split('/title ')[1]
    add(update, context)


def text(update, context):
    global data
    data[str(data.keys()).split("'")[-2]]['text'] = update.message.text.split('/text ')[1]
    add(update, context)


def image(update, context):
    dp.add_handler(MessageHandler(Filters.document, download))
    print(1)


def download(update, context):
    print(update.message)
    file_id = update.message.document.file_id
    newFile = context.bot.get_file(file_id)
    newFile.download('1.jpg')
    with open('1.jpg', 'rb') as file:
        global data
        data[str(data.keys()).split("'")[-2]]['image'] = str(file.read()).replace('"', "'")
    file.close()


def done(update, context):
    global data
    print(data)
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()
    start(update, context)


def help(update, context):
    update.message.reply_text(
        "/help - помощь \n /add - добавление статьи, следом надо выполнить в порядке , установленном в сообщении"
        " следующие команды: \n 1. /title заголовок (пример: /title Орден моего прадедушки) \n 2. /text текст статьи"
        "(пример: /text Этот орден был вручен дедушке в 1943 году и передается из поколение в поколение.) \n"
        "3. /image и в следом в отдельном сообщении отправить файл формата .jpg\n 4. /done - завершение статьи")


def main():
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


data = ''
updater = Updater(TOKEN)
dp = updater.dispatcher
if __name__ == '__main__':
    main()
