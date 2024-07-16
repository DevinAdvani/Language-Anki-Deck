import os
from main import *

#Make it so that multiword filenames work

folder_name = input("FOLDER NAME: ")
file_number = input("FILE AMOUNT: ")
try:
    os.mkdir(folder_name)
except:
    print("FILE ALREADY EXISTS")
for i in range(1,int(file_number) + 1):
    os.system("echo " + str(i) + " > " + folder_name + "/" + str(i) + ".txt")
