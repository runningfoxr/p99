import os
import shutil

source = input("Input source folder:- ")
destination = input('Input destination folder:- ')

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)