from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from data import config
from data.config import ip

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

#storage = MemoryStorage()
storage = RedisStorage2("localhost", 6379, db=5)


dp = Dispatcher(bot, storage=storage)
