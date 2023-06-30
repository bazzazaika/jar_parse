import var
from fs import *


def search_dang_func():
    dang_func = []
    with open(var.path_to_dang_func,"r") as f:
        for i in f.readlines():
            dang_func.append(i.replace("\n","")+'(')

    list = fs_file_list(var.path_to_output)
    for i in list:
        with open(i, 'r') as f:
            content = f.read()
            while content.find('import')!=-1:
                content = content[:content.find('import')]+content[content.find('\n')+1:]
            for j in dang_func:
                if content.find(j) != -1:
                    print(i," has dang func:", j)



search_dang_func()