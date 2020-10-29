import os
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.utils.executor import start_webhook

BOT_TOKEN = os.getenv("TOKEN")
WEBHOOK_HOST = "https://android-expert-bot.herokuapp.com/"
WEBHOOK_PATH = 'webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    pass

if __name__ == '__main__':
    from handlers import dp

    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WEBAPP_HOST, port=WEBAPP_PORT)