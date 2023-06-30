#this script needs to determine file extensions
import os
from queue import Queue
from fs import *

path = "E:\jar_parse\output"
file_list = fs_file_list(path)
extensions = set()
for i in file_list:
    if(i.find("my_path")==-1):
        extension = i.split(".")[-1]
        extensions.add(extension)
print(extensions)






