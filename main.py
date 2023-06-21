


from excel import read_files_from_directory,read_single_file
from emoji import extract_emoji_data
from word_cloud import create_most_used_word_cloud

columns=["Group","Student name","Student email","Reviewed work of student name","Criterion","Kind","Review"]
sheet_name='Reviews'
directory='data'

def main():
    data_frame=read_files_from_directory(directory,sheet_name,columns)
    #extract_emoji_data(data_frame,'Review',"Emoji")
    create_most_used_word_cloud("most_used.png",data_frame)
    #data_frame.to_excel("emoji_data.xlsx")
    

if __name__=="__main__":
    main()