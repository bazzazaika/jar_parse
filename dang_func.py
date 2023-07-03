from fs import *
import csv

def search_dang_func(mode,pt,path_to_dang_func):
    dang_func = []
    with open(path_to_dang_func,"r") as f:
        for i in f.readlines():
            dang_func.append(i.replace("\n",""))

    list = fs_file_list(pt)

    print("Start searching for dangerous functions")
    print("Progress:")
    mx = len(list)
    proz = 1
    kol = 0

    with open(pt+'.csv', 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['Path to jar-module', 'Java-class', 'Dangerous function'])
        for i in list:
            with open(i, 'r') as f_java:
                content = f_java.read()
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
                    parts = i.split('\\')
                    MAX = parts.index('output')
                    pt_to_jar = ''
                    for h in range(MAX+1+2):#+1 это само output, +2 остальные подкатологи до файла my_path
                        pt_to_jar += parts[h]+'\\'
                    with open(pt_to_jar+'my_path', 'r') as f_my_path:
                        full_path = f_my_path.read().replace("\n","")
                    writer.writerow([full_path,classes_found,j])
            kol+=1
            if(kol>=mx*0.1*proz):
                proz+=1
                print(kol,"/",mx)
    print("End searching")

