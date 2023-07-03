import os
import time
import fs


'''
list = fs.fs("C:\\Program Files\\UEMS_CentralServer")
kol = 0
start = time.time()
for i in list:
    if(kol<50):
        kol+=1
    else:
        break
    os.system("java -jar E:\\decompilers\\cfr.jar \""+i+"\" --outputdir trash\\")
end =  time.time()
cfr = end - start
print("cfr = ", end - start)
print()
print()
print()
print()
kol = 0
start = time.time()
for i in list:
    if(kol<50):
        kol+=1
    else:
        break
    os.system("java -jar E:\\decompilers\\procyon.jar \""+i+"\" -o trash\\")
end =  time.time()
print("procyon = ", end - start)
print("cfr = ",cfr)
'''

list = fs.fs("F:\\UEMS_CentralServer")
kol = 0
start = time.time()
for i in list:
    if(kol<50):
        kol+=1
    else:
        break
    os.system("E:\\decompilers\\jadx-master\\build\\jadx\\bin\\jadx "+i+ " -d E:\\tr")
end =  time.time()
print("jadx = ", end - start)




