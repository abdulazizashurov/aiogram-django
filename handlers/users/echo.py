from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from loader import dp


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    text = [
        f'Exo holati: {hcode(state)}',
        'Siz yuborgan habar: ',
        hcode(state)
    ]
    await message.answer('\n'.join(text))