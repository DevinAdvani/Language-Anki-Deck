import os

#Make it so that multiword filenames work

folder_name = input("FOLDER NAME: ")
language = input("LANGUAGE: ")
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
try:
    os.system("echo " + language + " > " + edited_folder_name + "/language" + ".txt")
except:
    pass