import re
from fs import *
import var


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def del_com():
    list = fs_file_list(var.path_to_output)
    mx = len(list)
    kol=0
    j = 1
    print("Start deleting comments")
    print("Progress:")
    for i in list:
        with open(i,'r') as f:
            content = f.read()
            tx = comment_remover(content)
        with open(i,'w') as f:
            f.write(tx)
        kol+=1
        if(kol>=mx*0.1*j):
            j+=1
            print(kol,"/",mx)
    print("End deleting comments")
        
