import os
import datetime

def create_dir(mode):
    # Получаем текущую дату и время
    now = datetime.datetime.now()
    # Преобразуем время в нормальный вид
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    formatted_time = formatted_time.replace(" ","_").replace(":","-")
    pt = "E:\\jar_parse\\output\\"+mode+"_"+formatted_time
    os.mkdir(pt)
    return pt
kol = 0
def nested_fold(pt,i):
    global kol
    parts = i.split("\\")
    name = parts[-1]
    new_pt = pt+'\\'+str(kol)
    kol+=1
    os.mkdir(new_pt)
    file = open(new_pt+"\my_path","w")
    file.write(i)
    file.close()
    return new_pt

def dec(mode, ptd, list):
    if(mode == "cfr"):
        pt = create_dir(mode)
        for i in list:
            pt_nested_fold = nested_fold(pt,i)
            #print("java -jar "+var.path_to_decompilers+"cfr.jar \""+i+"\" --outputdir "+pt_nested_fold)
            os.system("java -jar "+ptd+"cfr.jar \""+i+"\" --outputdir "+pt_nested_fold)
    elif(mode == "procyon"):
        pt = create_dir(mode)
        for i in list:
            pt_nested_fold = nested_fold(pt,i)
            #print("java -jar "+var.path_to_decompilers+"procyon.jar \""+i+"\" -o "+pt_nested_fold)
            os.system("java -jar "+ptd+"procyon.jar \""+i+"\" -o "+pt_nested_fold)

    else:
        print("This decompiler is not supported ")
        quit()
    return pt

