import asyncio
import logging
import webbrowser

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = '7075967497:AAHW5Py7j8iqZtuwDztsEwhwQNM2Trs9hmY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# @dp.message(CommandStart())
# async def begin(message: types.Message):
#     markup = InlineKeyboardMarkup()
#     but_1 = InlineKeyboardButton(text='Beginner', callback_data='but_1')
#     markup.add(but_1)
#     await bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
@dp.message(CommandStart())
async def handle_start(message: types.Message):
   await message.answer(text=f'Перейдите по команде /help, {message.from_user.first_name}!')


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    text = ('Выберите ваш уровень английского: \n/Beginner, '
            '\n/Elementary, \n/PreIntermediate, \n/Intermediate, \n/UpperIntermediate, \n/Advanced.'
            )
    await message.answer(text=text)


# @dp.message()
# async def echo_message(message: types.Message):
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text='Start processing...'
#     )
#     await message.answer(
#         text='Привет, я твой бот',
#     )
#     # await message.answer(text=message.text)
#     if message.text:
#         await message.reply(text=message.text)


# @dp.message(CommandStart())
# async def handle_start(message):
#     markup_inline = types.InlineKeyboardMarkup()
#     item_1level = types.InlineKeyboardButton(text='Beginner')
#     item_2level = types.InlineKeyboardButton(text='Elementary')
#     item_3level = types.InlineKeyboardButton(text='Pre-Intermediate')
#     item_4level = types.InlineKeyboardButton(text='Intermediate')
#     item_5level = types.InlineKeyboardButton(text='Upper-Intermediate')
#     item_6level = types.InlineKeyboardButton(text='Advanced')
#     markup_inline.add(item_1level, item_2level, item_3level, item_4level, item_5level, item_6level)
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text='Choose your level of English',
#         reply_markup=markup_inline
#     )
#
#     await message.answer(text=message.text)
#     if message.text:
#         await message.answer(
#             text='Sorry, I can not answer'
#         )


@dp.message(Command('Beginner'))
async def handle_beginner(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Основные грамматические темы, необходимые на начальном этапе:'
             '\nГлагол to be.'
             '\nЕдинственное и множественное число. Понятие «артикль».'
             '\nМестоимения.'
             '\nPresent Simple.'
             '\nНаречия частоты.'
             '\nPrepositions of time.'
             '\nОткрытые и закрытые вопросы, разница с be и do.'
             '\nCan и cant.'
             '\nLike, love, hate с герундием.'
             '\nPresent Continious.'
             '\nThere is/There are.'
             '\nPrepositions of place.'
    )


@dp.message(Command('Elementary'))
async def handle_elementary(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Грамматические темы, которые вы встретите помимо предыдущих из начального:'
             '\nПовелительное наклонение.'
             '\nPast Simple.'
             '\nIrregular verbs.'
             '\nThere was/There were.'
             '\nSome/any.'
             '\nMany/much и little/few, a lot of.'
             '\nИсчисляемые/неисчисляемые существительные.'
             '\nHow much/How many.'
             '\nПрилагательные сравнительное степени.'
             '\nПрилагательные превосходной степени.'
             '\nFuture Simple.'
             '\nTo be going to.'
             '\nPresent Perfect.'
    )


@dp.message(Command('PreIntermediate'))
async def handle_pi(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
    text='Грамматические темы на уровне Pre-Intermediate:'
         '\nСоюзы.'
         '\nPresent Continuous для будущих договоренностей.'
         '\nPast Continious.'
         '\nPast Simple и Past Continious в сложносочиненном предложении.'
         '\nPresent Perfect.'
         '\nPresent Perfect (for,since).'
         '\nРазница между Present Perfect и Past Simple.'
         '\nSomething/anything/nothing.'
         '\nToo/enough.'
         '\nWill/wont (спонтанные обещания, решения).'
         '\nУпотребление инфинитива.'
         '\nУпотребление герундия.'
         '\nМодальные глаголы (must, mustnt, have to, dont have to).'
         '\nRelative clause.'
         '\nМодальные глаголы (should, may, might).'
         '\nCould/Couldnt.'
         '\nWould like.'
         '\nНаречия.'
    )

    @dp.message(Command('Intermediate'))
    async def handle_i(message: types.Message):
        await bot.send_message(
            chat_id=message.chat.id,
            text='На среднем уровне актуальны следующие грамматические темы:'
                 '\nУсловные предложения первого и второго типов.'
                 '\nСтатичные и динамичные глаголы.'
                 '\nКонструкция used to/ didn’t use to, разница с would.'
                 '\nTo be used to/ to get used to.'
                 '\nКосвенная речь, разница между say и tell.'
                 '\nМодальные глаголы (might, must, can(t)) для предположений.'
                 '\nCan, could, be able to.'
                 '\nQuestion tags.'
                 '\nPast Perfect.'
                 '\nСогласование времен.'
                 '\nPresent Perfect Continious.'
                 '\nПассивный залог.'
        )


@dp.message(Command('UpperIntermediate'))
async def handle_ui(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='В грамматике же на данном этапе появляются некие тонкости, так как основные времена уже доведены до свободной практики.'
             '\nНулевой артикль.'
             '\nУказатели множества a little/little, a few/few, plenty of/ a lot of, all, every, both, no, none, every, most.'
             '\nThird conditional и Mixed conditional.'
             '\nthe ... the ...comparatives.'
             '\nРазница между Present Perfect и Present Perfect Continuous.'
             '\nNarrative tenses.'
             '\nFuture time clauses.'
             '\nКонструкции с wish.'
             '\nМодальные глаголы и перфектный инфинитив.'
             '\nVerbs of the senses.'
             '\nPassive Voice.'
             '\nWhatever, whenever, whoever.'
             '\nPast Perfect Continuous, Future Continuous, Future Perfect.'
    )


@dp.message(Command('Advanced'))
async def handle_a(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='На высоком уровне вы встретите такие новые грамматические темы.'
             '\nСмешанный тип условных предложений.'
             '\nИнверсия.'
             '\nОбороты с get и have.'
             '\nПунктуация.'
             '\nEllipsis.'
             '\nFuture Perfect Continuous.'
             '\nFuture in the Past.'
             '\nCleft sentences.'
             '\nWishes and regrets.'
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
