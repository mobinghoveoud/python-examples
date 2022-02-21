import glob
import os


def getFiles(folder):
    allFile = []
    os.chdir(folder)
    for i in glob.glob("*"):
        if (os.path.isdir(folder + "/" + i)):
            all = getFiles(folder + "/" + i)
            for j in all:
                allFile.append(j)

        if (os.path.isfile(folder + "/" + i)):
            allFile.append(i)
    return allFile


path = os.path.abspath(".")
allFile = getFiles(path)

os.chdir(path)
# this way is more ram friendly. 
with open("index.txt", "a") as f:
    for file in allFile:
        f.write(file + "\n")
