import sys

users = []
tasks = []
userTask = []
n = 0


if (len(sys.argv) > 1):
    if (sys.argv[1] == "--help"):
        print("--help => help\n-n     => Number of commands\n\ninput example:\nCREATE USER X\nCREATE TASK Y\nASSIGN Y X\nLIST USER X\nLIST TASK Y")
        exit()
    
    if (sys.argv[1].find("-n") != -1):
        n = sys.argv[1].split("=")[1]

for i in range(int(n)):
    text = input()

    if (text == "0"):
        break

    text = text.split()

    if (text[0] == "CREATE"):
        if (text[1] == "USER"):
            users.append(text[2])
        if (text[1] == "TASK"):
            tasks.append(text[2])

    if (text[0] == "ASSIGN"):
        userId = users.index(text[2])
        taskId = tasks.index(text[1])

        if (userId == -1 or taskId == -1):
            print("Wrong! try again:\n")
            continue

        # [userId, taskId]
        userTask.append([userId, taskId])

    if (text[0] == "LIST"):
        if (text[1] == "USER"):
            for i in userTask:
                if (users[i[0]] == text[2]):
                    print(tasks[i[1]])
        if (text[1] == "TASK"):
            for i in userTask:
                if (tasks[i[1]] == text[2]):
                    print(users[i[0]])
