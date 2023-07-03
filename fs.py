#my
from classes import *
#python modules
import os
from queue import Queue

def fs_file_list(path):
    file_list = []
    queue_dir = Queue()#create queue for dir
    dr = DIR(path,path)
    queue_dir.put(dr)
    while queue_dir.qsize()!=0:
        dr = queue_dir.get()
        path = dr.ret_path()
        entries = os.scandir(path)
        for entry in entries:
            if entry.is_file():
                #print(entry.name)
                file_list.append(path+'\\'+str(entry.name))
            elif entry.is_dir():
                dr = DIR(str(entry.name),path+'\\'+str(entry.name))
                queue_dir.put(dr)
    return file_list

def fs(path_to_server):
    try:
        os.chdir(path_to_server)#change initial dir
    except:
        print("Unknow initial directory! Exit...")
        quit()
    path = path_to_server
    file_list = fs_file_list(path)
    jar_files=[]
    
    for i in file_list:
        if(i.endswith(".jar")):
            jar_files.append(i)
        file_list = []

    return jar_files
    '''
    for i in jar_files:
        print(i)
    print(len(jar_files))
    '''