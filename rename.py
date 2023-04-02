import os

filesRename = ['text1.txt','text2.txt','text3.txt']
directory = os.getcwd()

# Iterate
for file in os.listdir(directory):
	# Checking if the file is present in the list
	if file in filesRename:
		oldName = os.path.join(directory, file)
		n = os.path.splitext(file)[0]

		b = n + "_new" + '.txt'
		newName = os.path.join(directory, b)

		# Rename the file
		os.rename(oldName, newName)

res = os.listdir(directory)
# print(res)

print(res)