from cmath import inf
import json


def sortById(value):
    return value["id"]


inputFile = input()
outputFile = input()

inFile = open(inputFile, "r")
textJson = []

lines = inFile.readlines()
for line in lines:
    textJson.append(json.loads(line))
inFile.close()

textJson.sort(key=sortById)
print(textJson)

outFile = open(outputFile, "w")
for line in textJson:
    outFile.write(json.dumps(line))
outFile.close()
