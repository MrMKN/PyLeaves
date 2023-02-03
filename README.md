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
        ud_type := "try to download......", # must be a string 
        message := editable_text, # editable message 
        start := start_time # time.time() import time.time  & time()
        template := PROGRESS_BAR, # progress template check more description 
        finished_str := '▣', # string character for identifie the finished percentage 
        unfinished_str := '▢', # string character for identifie the unfinished percentage
        markup := Button, # pyrogram replay_markup 
        )
    )       

# ⚠️ don't use  =  must use  :=

```


### formats of template

* {current} = process completed file size
* {total} = total file size 
* {percentage} = total completed percentage 
* {speed} = current speed in byte/second 
* {est_time} = estimated time 










