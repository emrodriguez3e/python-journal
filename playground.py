import os
import time

created_list = []

for i in os.listdir('noteDirectory'):
    a = os.stat(os.path.join('noteDirectory',i))
    # print(i, " :: ", str(time.ctime(a.st_atime)))
    created_list.append([time.ctime(a.st_ctime), i])

for i in sorted(created_list):
    print(i)



