#https://stackoverflow.com/questions/43146528/how-to-extract-all-the-emojis-from-text

import demoji
import pandas as pd

def count_emojis(data):
    emoji_count=0
    for comment in data:
        if (type(comment) == str):
            emoji_count+=len(demoji.findall_list(comment))
            
    return emoji_count
