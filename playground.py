import os
noteFolder = []

currentPath = os.getcwd()
print(os.listdir(currentPath))


noteDirectory = os.path.join(currentPath, 'noteDirectory')




if not os.path.isdir(noteDirectory):

    os.mkdir(currentPath + "\\noteDirectory")

    for i in range(1,11):
        file = open("noteDirectory\\untitled"+str(i)+".txt", 'w')
        file.close()
        print("File has been created")
else:
    pass

# This gets the list of notes that are within the directory
print(os.listdir(noteDirectory))

os.remove(noteDirectory)
