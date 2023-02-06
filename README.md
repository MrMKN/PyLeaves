# PyLeaves

🌿 telegram bot's python pypi package & tools for pyrogram

### Current featur ⚡️

progress_for_pyrogram():

This is async function of ( Download | Upload ) progress bar with simple way to use

### Example

``` python

# import time.time and other 
from pyleaves import Leaves # must import 

PROGRESS_BAR = """
percentage: {percentage} | {current}
total completed: {total}%
current speed: {speed}/s
estimate time: {est_time} """

Button = InlineKeyboardMarkup([[InlineKeyboardButton('text', callback_data="data")]])

start_time = time()
editable_text = await app.send_message(chat_id, "download started")

# download media 
await app.download_media(
    message,
    progress=Leaves.progress_for_pyrogram,
    progress_args=(
        "try to download......", # 1. must be a string 
        editable_text, # 2. editable message 
        start_time # 3. time.time() import time.time  & time()
        PROGRESS_BAR, # 4. progress template check more description 
        '▣', # 5. string character for identifie the finished percentage 
        '▢', # 6. string character for identifie the unfinished percentage
        Button, # 7. pyrogram replay_markup 
        )
    )       

# ⚠️ don't use  parameters keyword & must keep this Oder 

```


### formats of template

* {current} = process completed file size
* {total} = total file size 
* {percentage} = total completed percentage 
* {speed} = current speed in byte/second 
* {est_time} = estimated time 










