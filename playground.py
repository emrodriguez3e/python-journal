import os



for i in os.listdir('noteDirectory'):
    if not i == '.DS_Store':
        file = open('noteDirectory/'+i)
        print('File ' + str(i) + " has been opened")
        file.close()