import os
import asyncio
from urllib.parse import urljoin
from aiohttp import web
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.webhook import get_new_configured_app
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv("TOKEN"))
WEBHOOK_HOST = str(os.getenv("WEBHOOK_HOST"))
WEBHOOK_URL_PATH = '/webhook/' + BOT_TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

async def on_startup(app):
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == '__main__':
    from handlers import dp

    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    app.on_startup.append(on_startup)
    web.run_app(app, host='0.0.0.0', port=os.getenv('PORT'))