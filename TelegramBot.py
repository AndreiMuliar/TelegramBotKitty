import time
from random import choice
from PIL import Image, ImageDraw, ImageFont
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from database import insert_varible_into_table

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=graph(choice([f"kitty{i}.jpg" for i in range(1, 4)])))
    insert_varible_into_table(update.message.from_user.id)


def graph(photo):
    tm = time.localtime()
    img = Image.open(photo)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("ComicSansMS3.ttf", int(min((img.width / 2, img.height / 2)) // 6))
    draw.text((80, img.height - 180), time.strftime("%Y-%m-%d %H:%M:%S", tm), (255, 255, 255), font=font)
    img.save('update_kitty.jpg')
    return "update_kitty.jpg"


if __name__ == '__main__':
    application = ApplicationBuilder().token("5997551557:AAE1xEK7N_aa8mUzqsFjhNAiLYy5ZByncn4").build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
