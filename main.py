
from aiogram.utils import executor
import logging
from config import dp
from handlers import callbek, klient,extra,admin, fsm_admin

klient.register_handlers_klient(dp)
callbek.register_callbek_hansdlers(dp)
admin.register_handlers_admin(dp)
fsm_admin.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates= True)

