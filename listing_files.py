import os

cwd = os.getcwd()

my_dir = os.listdir(cwd)

i = 0
for my_files in my_dir:
    # source = my_files + my_dir
    my_dest = "new" + str(i) + ".txt"
    my_source = cwd + my_dest

    print(my_dest)

# print(my_dir)