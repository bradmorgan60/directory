from asyncore import file_dispatcher
import os
import time
import shutil

# cwd = os.getcwd()
# print(cwd)

# os.listdir()


def move_to_downloads():
    file=input("Input file here: ")

    path1 = f"/Users/bradmorgan60/OneDrive/Documents/bash/{file}"
    path2 = "/Users/bradmorgan60/downloads"

    shutil.move(path1, path2)

# move_to_downloads()

def move_from_downloads():
    file=input("Input file here: ")

    path1 = "/Users/bradmorgan60/OneDrive/Documents/bash/"
    path2 = f"/Users/bradmorgan60/downloads/{file}"

    shutil.move(path2, path1)

move_from_downloads()



# def rename_files():
#     for file_name in os.list_dir(cwd):
#         source = cwd + file_name





