from aiogram import types
from create_bot import bot
from model import total_candies


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!'
                                                 f' Сегодня будем делить конфеты. Сейчас их {total_candies}')
async def goodbye(message: types.Message):
    await bot.send_message(message.from_user.id, f'Пока {message.from_user.first_name}!'
                                                 f' С тобой было приятно поиграть')