import os,sys

# print(os.name)                  #Display the OS name ->nt
# print(os.getcwd())              #Display Current Working Directory # To print absolute path on your system # os.path.abspath('.')  
  
# print(os.listdir('.'))          # To print files and directories in the current directory on your system

# fd = "GFG.txt"

# # popen() is similar to open() 
# file = open(fd, 'w') 
# file.write("Hello") 
# file.close() 
# file = open(fd, 'r') 
# text = file.read() 
# print(text) 

# # popen() provides a pipe/gateway and accesses the file directly 
# file = os.popen(fd, 'w') 
# file.write("Hello") 
# # File not closed, shown in next function. 
# fd = "GFG.txt"
# os.rename(fd,'New.txt') 
# os.rename(fd,'New.txt')

# print(sys.version)
# print(sys.version_info)
# print("Hello {}".format(sys.argv))

# print(sys.maxsize)     # Returns the largest integer a variable can take.
# print(sys.path)           #Returns all required paths







