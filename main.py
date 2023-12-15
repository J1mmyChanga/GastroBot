import asyncio
import logging
import sys
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import utils.queue_state as state

from handlers import *


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    scheduler = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
    scheduler.add_job(state, trigger='interval', seconds=15, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())