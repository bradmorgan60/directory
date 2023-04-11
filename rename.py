
#!/usr/bin/env python3

import os
import shutil
import time

filesRename = ['text1.txt','text2.txt']
downloads = "/Users/bradmorgan60/Downloads/"
dest_directory = os.getcwd()
# print(dest_directory)

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

# rename_move2()

def move_file():
	for file in os.listdir(downloads):
		if file.endswith('.txt'):

			oldPath = os.path.join(dest_directory, file)
			newPath = os.path.join(dest_directory, file)
			
			# # downloads = f"/Users/bradmorgan60/downloads/{file}"
			os.rename(oldPath, newPath)

			# print(f"Renamed {file} to {newFile}")
			shutil.copy(newPath, dest_directory)
			print(f"{newPath} moved to current directory...")
	
move_file()

# print(os.listdir(downloads))

