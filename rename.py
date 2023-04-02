from hashlib import new
import os

filesRename = ['text1.txt','text2.txt']
directory = os.getcwd()

# Iterate
def rename():
	for file in os.listdir(directory):
		# Checking if the file is present in the list
		if file in filesRename:
			oldName = os.path.join(directory, file)
			n = os.path.splitext(file)[0]

			b = n + "_new" + '.txt'
			newName = os.path.join(directory, b)

			# Rename the file
			os.rename(oldName, newName)
			print(f"Renamed {oldName} to {newName}")

	# res = os.listdir(directory)
	

# rename()

def rename2():
	for file in os.listdir(directory):
		if file.endswith('.txt'):
			newFile = f"new_{file}"

			oldPath = os.path.join(directory, file)
			newPath = os.path.join(directory, newFile)

			os.rename(oldPath, newPath)

			print(f"Renamed {file} to {newFile}")

rename2()



