# Copyright (©) 2023 https://github.com/MrMKN
# Telegram Link : https://t.me/Mr_MKN 
# Repo Link : https://github.com/MrMKN/PyLeaves
# License Link : https://github.com/MrMKN/PyLeaves/blob/main/LICENSE

import math, time
from pyleaves.utils import *
from pyleaves.text_format import *
from pyrogram.types import *


async def pyro_progress(
    current,
    total,
    ud_type,
    message,
    start,
    template=PROGRESS_BAR,    
    finished_str='●',
    unfinished_str='○',
    markup=None,
):

    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)


        progress = "{0}{1}".format(
            ''.join([finished_str for i in range(math.floor(percentage / 5))]),
            ''.join([unfinished_str for i in range(20 - math.floor(percentage / 5))]))
           
        tmp = progress + template.format( 
            percentage=round(percentage, 2),
            current=humanbytes(current),
            total=humanbytes(total),
            speed=humanbytes(speed),
            est_time=estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(text=f"{ud_type}\n\n{tmp}", reply_markup=markup)                       
        except Exception as e:
            print(e)





