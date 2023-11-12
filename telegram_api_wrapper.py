import asyncio
import os

from telethon.sync import TelegramClient
from telethon.tl.patched import Message

import google_api_wrapper
import dotenv

dotenv.load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
allowed_chat_list = [
    'Группа 1 - НС4 - Анастасия',
    'Группа 2 - НС4 - Владимир',
    'Группа 3 - НС4 - Фарида',
    'Общий чат - Нейроспринт 4.0. Восстание машин'
]

async def create_telegram_client():
    client = TelegramClient('2724818', int(api_id), api_hash)
    await client.start()
    return client


async def main():
    client = await create_telegram_client()
    chats = await client.get_dialogs()
    response = []
    for chat in chats:
        if chat.name in allowed_chat_list:
            print(chat.name)
            messages = await client.get_messages(entity=chat)
            for message in messages:
                if isinstance(message, Message):
                    response.append([message.message, chat.name])
    google_api_wrapper.write(response)
if __name__ == '__main__':
    asyncio.run(main())
