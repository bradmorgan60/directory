from asyncore import file_dispatcher
import os
import time
import shutil

# cwd = os.getcwd()
# print(cwd)

# os.listdir()

downloads = "/Users/bradmorgan60/Downloads/"
current_dir = os.getcwd()

def move_to_downloads():
    file=input("Input file here: ")

    path1 = f"/Users/bradmorgan60/OneDrive/Documents/directory/{file}"
    path2 = "/Users/bradmorgan60/downloads"

    shutil.move(path1, path2)

# move_to_downloads()

def move_from_downloads():
    file=input("Input file here: ")

    downloads_file = f"/Users/bradmorgan60/Downloads/{file}"

    shutil.move(downloads_file, current_dir)

# move_from_downloads()

def copy_pdf():
    for file in os.listdir(downloads):
        if file.endswith("pdf"):
            c = f"/Users/bradmorgan60/Downloads/{file}"

            shutil.copy(c, current_dir)
            print(f"{file} has been copied to current directory")

copy_pdf()
# def rename_files():
#     for file_name in os.list_dir(cwd):
#         source = cwd + file_name





