import datetime
import time

# TODO: The issue is how to name the file

'''
File name should be (DateString)(TimeString)
YYYYMMDD
HHMMSS(MSMSMS)
Including milliseconds, accuracy of 3 digits. 
'''

print(str(datetime.date.today()).replace("-", ""))
print(time.localtime())

local = time.localtime()
time_stamp = time.time()


print("File name is: " +
      str(local.tm_year) + "-" +
      str(local.tm_mon) + "-" +
      str(local.tm_mday) + "-" +
      str(local.tm_hour) + "-" +
      str(local.tm_min) + "-" +
      str(local.tm_sec) + "-" +
      str(int(round((time.time() % 1), 2)*100) )+".txt")

