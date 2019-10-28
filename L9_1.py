
# data = file.readlines()
# print(data)
# print(len(data))
# for i in data:
#     print(len(i))
#     j = i.split(' ')
#     print(len(j))
name = 0
surname = 1
clas = 2
DOB = 3

path = (r'C:\Users\mykhailo.holovko\PycharmProjects\Test 123\venv\L9_pr2.txt')

def readDB(path):
    users = []
    for line in open(path):
        tUser = []
        for i in line.split(' '):
            tUser.append(i.split('=')[1])
        users.append(tUser)
    return users

def printDB(dbUsers):
    for user in dbUsers:
        print('name = %-12s surName = %-12s clas = %-5s DOB = %-10s' % (user[name], user[surname] ,user[clas] ,user[DOB]), end = '')

def older(arg1, arg2):
    if int(arg1[2]) < int(arg2[2]):
        return True
    elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) < int(arg2[1]):
        return True
    elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) == int(arg2[1]) and int(arg1[0]) < int(arg2[0]):
        return True
    else:
        return False

def OlderPerson(dbName):
    iOlderUser = 0
    for i  in range(1, len(dbName)):
        date = dbName[i][DOB].split('.')
        dateOlder = dbName[iOlderUser][DOB].split('.')
        if older(date, dateOlder):
            iOlderUser = i
    return iOlderUser

def younger(arg1, arg2):
    if int(arg1[2]) > int(arg2[2]):
        return True
    elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) > int(arg2[1]):
        return True
    elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) == int(arg2[1]) and int(arg1[0]) > int(arg2[0]):
        return True
    else:
        return False

def youngestPerson(dbName):
    iYoungUser = 0
    for i in range(1, len(dbName)):
        date = dbName[i][DOB].split('.')
        dateYounger = dbName[iYoungUser][DOB].split('.')
        if younger(date, dateYounger):
            iYoungUser = i
    return iYoungUser

users = readDB(path)
printDB(users)
print('')
oldest = OlderPerson(users)
#print('\n',users[oldest])
print('\n''The most Oldest: ')
print('name = %-12s surName = %-12s class = %-5s DOB = %-10s' % (users[oldest][name], users[oldest][surname], users[oldest][clas], users[oldest][DOB]))

youngest = youngestPerson(users)
#print('\n',users[youngest])
print('The most youngest: ')
print('name = %-12s surName = %-12s class = %-5s DOB = %-10s' % (users[youngest][name], users[youngest][surname], users[youngest][clas], users[youngest][DOB]))