# OS Module in Python

# OS stands for operating systems like windows, linux etc
# OS module is a build in module of python. Using OS module, we can rename-optimize the files or
# folders and many other function

import os

print(dir(os))

# get your current working directory ( getcwd() )
print(os.getcwd())

# Change your current working directory using chdir()
# os.chdir("C://")
# print(os.getcwd())

# Read file
# it only reads the files which is available in your current working directory.
# If you changed the directory then it reads the files of that directory

f = open("myfile.txt")
readNow = f.read()
print(readNow)

# listdir() : It returns your all the files which is available in your current directory
print(os.listdir())
print(os.listdir("C://"))

# making a directory using mkdir()
# os.mkdir("newFile")

# making a directories and his sub files using makedirs(). It is used to making subdirectories automatically
# os.makedirs("newFile1/newFile2")

# Rename a directory
# os.rename("newFile", "newFileRenamed")

# read environment variable
print(os.environ.get('PATH'))

# join() : To join two paths
print(os.path.join("C://", "joinedFile.txt"))

# If the path or directory is exists it returns True, else False
print(os.path.exists("C://"))

# If directory exits it returns True, else False
print(os.path.isdir("C://"))

# If file exists it returns True, else False
print(os.path.isfile("myfile.txt"))




