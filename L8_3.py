def readMass(path):
    file = open(path)
    N = 0
    mass = []
    for line in file:
        row = line.strip().split('  ')
        mass.append(row)
        N += 1
    file.close()
    return mass, N

def printMass(mass,N):
    for i in range(N):
        for j in range(N):
            print('%5s' %mass[i][j], end='')
            #print("%4d" % mass[i][j], end='')
            #print(j, end = ' ')
        print()

def printList(list):
    print('%4s'%'Here is the sum per coulumn: ')
    for i in range(len(list)):
        print('%5s' %list[i], end='')
            #print("%4d" % mass[i][j], end='')
            #print(j, end = ' ')
    print()


def change(mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if i == j:
                mass[i][j], mass[i][len(mass) - 1 - j] = mass[i][len(mass) - 1 - j] , mass[i][j]
    return mass

def getSumByColumn(mass):
    colSum = []
    for i in range(len(mass)):
        sum = 0
        for j in range(len(mass)):
            sum += int(mass[j][i])
        colSum.append(sum)
    #print(type(colSum))
    return colSum

def maxElem(list):
    temp = 0
    colNum = 0
    for i in range(len(list)):
        if temp < int(list[i]):
            temp = int(list[i])
            colNum = i
    return  colNum,temp

# def getSumByRow(mass):
#     rowSum = []
#     for i in range(len(mass)):
#         sum = 0
#         for j in range(len(mass)):
#             sum += int(mass[i][j])
#         rowSum.append(sum)
#     # print(type(colSum))
#     return rowSum

mass, N = readMass(r'C:\Users\mykhailo.holovko\PycharmProjects\Test 123\venv\file_2.txt')
printMass(mass,N)
#print(getSumByColumn(mass))
#print(type(mass))
printList(getSumByColumn(mass))
#res = change(mass)
print()
print('Number of coulumn and max Value are:: ', maxElem(getSumByColumn(mass)))

#printMass(mass,N)
#print(getSumByRow(mass))