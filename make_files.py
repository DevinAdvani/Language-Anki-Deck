import os

#Make it so that multiword filenames work

folder_name = input("FOLDER NAME: ")
file_number_start = input("FILE NUMBER START: ")
file_number_end = input("FILE NUMBER END: ")

edited_folder_name = ""
for i in range(0,len(folder_name)):    
    if (folder_name[i] == " "):
        edited_folder_name += '_'
    else:
        edited_folder_name += folder_name[i]

for i in range(int(file_number_start), int(file_number_end) + 1):
    os.system("echo " + str(i) + " > " + edited_folder_name + "/Paragraph_" + str(i) + ".txt")