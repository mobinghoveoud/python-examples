def sliceInt(num):
    newNum = []
    if (len(num) % 3 != 0):
        newNum.append(num[0:len(num) % 3])

    for i in range(len(num) % 3, len(num), 3):
        newNum.append(num[i:i+3])
    print(",".join(newNum))


num = input()
sliceInt(num)
# print(num.split())
