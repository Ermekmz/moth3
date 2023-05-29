
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from config import bot, ADMIN
from keibort import klient_kb
import uuid

print(uuid.uuid1())
gen_id=uuid.uuid1()

class FSMadmin(StatesGroup):

    name = State
    age = State
    naprovlenie = State
    group = State
    photo = State
    submit = State

async def fsm_start(message : types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('ты не достоин!')
        else:
            await message.answer(f'{gen_id}')
            await FSMadmin.name.set()
            await message.answer('КТО ТЫ?!',reply_markup=klient_kb.cancle_markup)

    else:
        await message.answer('пиши в личке!!!')
async def new_name(message : types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['id'] = gen_id
        data['username'] = f'@{message.from_user.username}'
        data['name'] = message.text
    await FSMadmin.next()
    await message.answer('Сколько лет?')

async def new_age(message : types.Message,state:FSMContext):
    if not message.text.isdigit():
        await message.answer('Пиши только числа')
    elif int(message.text) < 10 or int(message.text) > 19:
        await message.answer('Ты слишком стар или ещё не дорос')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMadmin.next()
        await message.answer('Напрвление?',reply_markup=klient_kb.napr_markup)

async def new_napr(message : types.Message,state:FSMContext):
    if message.text not in ['Backend','Frontend','UX-UI','Android','IOS']:
        await message.answer('Выбери из списка!!!')
    else:
        async with state.proxy() as data:
            data['naprovlenie'] = message.text
        await FSMadmin.next()
        await message.answer('Какая группа?',reply_markup=klient_kb.cancle_markup)

async def new_group(message : types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMadmin.next()
    await message.answer('PHOTO?')

async def new_photo(message : types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(data['photo'],caption=f"{data['name']}\n{data['age']}\n"
                                                         f"{data['naprovlenie']}\n{data['group']}\n"
                                                         f"{data['username']}\n {gen_id}"
                                   )
    await FSMadmin.next()
    await message.answer('Всё норм?',reply_markup=klient_kb.submit_markup)


async def submit(message : types.Message,state:FSMContext):
    if message.text.lower() == 'да':
        await state.finish()
        await message.answer('не темик')
    elif message.text.lower == 'нет':
        await state.finish()
        await message.answer('темик')
    else:
        await message.answer('не понятно')

async def cancle_fsm(message : types.Message,state:FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('темик')

def register_handlers_fsm(dp :Dispatcher):
    dp.register_message_handler(cancle_fsm,state='*',commands='cancle')
    dp.register_message_handler(cancle_fsm, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start,commands=['reg'])
    dp.register_message_handler(new_name, state=FSMadmin.name)
    dp.register_message_handler(new_age, state=FSMadmin.age)
    dp.register_message_handler(new_napr, state=FSMadmin.naprovlenie)
    dp.register_message_handler(new_group, state=FSMadmin.group)
    dp.register_message_handler(submit, state=FSMadmin.submit)
