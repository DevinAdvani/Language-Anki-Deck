import os
from main import *

#Make it so that multiword filenames work

folder_name = input("FOLDER NAME: ")
file_number = input("FILE AMOUNT: ")
edited_folder_name = ""
for i in range(0,len(folder_name)):    
    if (folder_name[i] == " "):
        edited_folder_name += '_'
    else:
        edited_folder_name += folder_name[i]
try:
    os.mkdir(edited_folder_name)
except:
    print("FILE ALREADY EXISTS")
for i in range(1,int(file_number) + 1):
    os.system("echo " + str(i) + " > " + edited_folder_name + "/Paragraph_" + str(i) + ".txt")