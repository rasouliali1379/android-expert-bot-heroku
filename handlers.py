import requests
import os
from dotenv import load_dotenv

from main import bot, dp
from aiogram.types import Message
from config import question_no_content, channel_id
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler()
async def echo(message: Message):
    content = message.text.strip()
    if content.startswith("#سوال"):
        if len(content) > 5:
            question = content.replace("#سوال", "")
            id = message["from"]["id"]
            load_dotenv()
            COMMENT_BOT_TOKEN = str(os.getenv('COMMENT_BOT_TOKEN'))
            base_url = f"https://api.comments.bot/createPost?api_key={COMMENT_BOT_TOKEN}&owner_id={id}&type=text&text={question}"

            result = requests.get(base_url)
            result = result.json()
            username = message["from"]["username"]
            question = question + f"\n\nسوال پرسیده شده توسط @{username}"
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
            channel_post = await bot.send_message(chat_id=channel_id,
                                text= question,
                                reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="پاسخ ها", url= result["result"]["link"]),]],resize_keyboard=True) )
            
            await bot.forward_message(chat_id=message.chat.id,
                                from_chat_id = channel_post["chat"]["id"],
                                message_id = channel_post["message_id"])
        else:
            await bot.send_message(chat_id=message.chat.id, text=question_no_content)
