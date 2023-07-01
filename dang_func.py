import var
from fs import *
import csv

def search_dang_func(mode,pt):
    dang_func = []
    with open(var.path_to_dang_func,"r") as f:
        for i in f.readlines():
            dang_func.append(i.replace("\n",""))

    list = fs_file_list(pt)

    print("Start searching for dangerous functions")
    print("Progress:")
    mx = len(list)
    proz = 1
    kol = 0

    with open(pt+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path to jar-module', 'Java-class', 'Dangerous function'])
        for i in list:
            with open(i, 'r') as f:
                content = f.read()
                '''
                while content.find('import')!=-1:
                    start = content.find('import')
                    end = content.find('\n')+1
                    if end <= start:
                        content = content[end:]+content[:end]
                        continue
                    content = content[:start]+content[end:]
                '''
                flag = False
                classes_found = '-'
                for j in dang_func:
                    if content.find(j+'(') != -1:
                        ind = content.find('class')
                        if ind != -1:
                            parts = i.split('\\')
                            name = parts[-1]
                            name = name.split('.')
                            name = name[0]
                            '''
                            if name == 'FilterBuilder':
                                print()
                            '''
                            
                            h = ind
                            while(content[h]!=' '):#первое слово(class)
                                h+=1
                            h+=1
                            classes_found = ''
                            while(content[h]!=' ' and content[h]!='\n' and len(classes_found)<=len(name) and content[h]!='<'):
                                classes_found += content[h]
                                h+=1
                            if(classes_found != name):
                                classes_found = '-'

                        #print(i," has dang func:", j)
                        flag = True
                        break
                if flag:
                    writer.writerow([i,classes_found,j])
            kol+=1
            if(kol>=mx*0.1*proz):
                proz+=1
                print(kol,"/",mx)
    print("End searching")

