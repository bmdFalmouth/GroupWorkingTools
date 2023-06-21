

import demoji
import pandas as pd

def count_emojis(data):
    emoji_count=0
    for comment in data:
        if (type(comment) == str):
            emoji_count+=len(demoji.findall_list(comment))
            
    return emoji_count

def extract_emoji_data(data,source_column,dest_column):
    print("Extracting Emojis")
    data[dest_column]="None"
    index=0
    for entry in data[source_column]:
        if (type(entry)==str):
            emojis=demoji.findall_list(entry)
            emoji_str=""
            for emjoi in emojis:
                emoji_str+=emjoi+" "
            
            data.at[index,dest_column]=emoji_str
        index+=1
            
            
