import os 
import shutil
from turtle import down

cur_dir = os.getcwd()
downloads = "/Users/bradmorgan60/Downloads"
elle = "/Users/bradmorgan60/OneDrive/apartment/Elle 2023-2024"
name = "Elle of Buckhead directory"

def move_to_directory():
    for file in os.listdir(downloads):
        if file.startswith('demo') or file.endswith(".txt"):
            d = f"/Users/bradmorgan60/Downloads/{file}"

            shutil.move(d, cur_dir)
            print(f"{file} moved to working directory")
        
        if file.endswith(".pdf") or file.endswith('.eml'):
            d = f"/Users/bradmorgan60/Downloads/{file}"
            elle = "/Users/bradmorgan60/OneDrive/apartment/Elle 2023-2024"
            name = "Elle of Buckhead directory"

            shutil.move(d, elle)
            print(f"{file} moved to {name}")
        
        if file.endswith(".txt") and file.startswith('demo'):
            d = f"/Users/bradmorgan60/Downloads/{file}"
            name = "current directory"

            shutil.move(d, cur_dir)
            print(f"{file} moved to {name}")

move_to_directory()

# This function will move files in current directory back to downloads
def move_to_downloads():
    for file in os.listdir(cur_dir):
        if file.endswith(".txt") or file.startswith('demo'):
            c = f"{cur_dir}/{file}"
            downloads = "/Users/bradmorgan60/Downloads"

            shutil.move(c, downloads)
            print(f"{file} moved from current directory to downloads...")
    
        for file in os.listdir(elle):
            if file.endswith('.txt') or file.startswith('demo'):
                shutil.move(elle, downloads)
                print('Files moved from apartment folder to downloads')

        

# move_to_downloads()

# print(os.getcwd())

