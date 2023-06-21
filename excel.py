import os
import pandas as pd

def read_single_file(filename,sheet_name=None,columns=None):
    data_frame=pd.read_excel(filename,sheet_name=sheet_name,usecols=columns)
    return data_frame


def read_files_from_directory(dir,sheet_name=None,columns=None):
    print("Read all excel files")
    #create empty data frame
    results=pd.DataFrame()
    #check to see if value passed in is a dir
    if (os.path.isdir(dir)):
        files=os.listdir(dir)

        # process files
        for file in files:
            path=os.path.join(dir,file)
            
            #if we have found another dir, call function recursilvely
            if (os.path.isdir(path)):
                results=pd.concat([results,read_files_from_directory(path,sheet_name,columns)],ignore_index=True)
            elif (file.endswith('.xlsx') or file.endswith('.xls')):
                #Read data from excel and concat
                print(file)
                data_frame=pd.read_excel(path,sheet_name=sheet_name,usecols=columns)
                results =pd.concat([results,data_frame], ignore_index=True)

    return results
    
