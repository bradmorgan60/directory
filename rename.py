
#!/usr/bin/env python3

import os
import shutil
import time
from turtle import down


filesRename = ['text1.txt','text2.txt']
downloads = "/Users/bradmorgan60/downloads"
dest_directory = os.getcwd()

# Iterate
def rename():
	for file in os.listdir(dest_directory):
		# Checking if the file is present in the list
		if file in filesRename:
			oldName = os.path.join(dest_directory, file)
			n = os.path.splitext(file)[0]

			b = n + "_new" + '.txt'
			newName = os.path.join(dest_directory, b)

			# Rename the file
			os.rename(oldName, newName)
			print(f"Renamed {oldName} to {newName}")

	# res = os.listdir(dest_directory)
	
# rename()

# Rename file and copy it to your downloads folder
def rename_copy():
	for file in os.listdir(dest_directory):
		if file.endswith('.txt') | file.startswith('T'):
			newFile = f"new_{file}"

			oldPath = os.path.join(dest_directory, file)
			newPath = os.path.join(dest_directory, newFile)

			os.rename(oldPath, newPath)

			print(f"Renamed {file} to {newFile}")
			
			shutil.copy(newPath, downloads)

# rename_move()

# Use this function to copy text files from downloads to your current directory
def rename_copy2():
	for file in os.listdir(downloads):
		if file.endswith('.txt') | file.startswith('T'):
			newFile = f"{file}"

			oldPath = os.path.join(downloads, file)
			newPath = os.path.join(downloads, newFile)

			os.rename(oldPath, newPath)

			# print(f"Renamed {file} to {newFile}")
			
			shutil.copy(newPath, dest_directory)
			print(f"{file} has been moved...")

rename_move2()


def rename3():
	for file in os.listdir(dest_directory):
		if file.startswith('t'):
			newFile = f"new_{file}"

			oldPath = os.path.join(dest_directory, file)
			newPath = os.path.join(dest_directory, newFile)

			os.rename(oldPath, newPath)

			print(f"Renamed {file} to {newFile}")
	
# rename3()

