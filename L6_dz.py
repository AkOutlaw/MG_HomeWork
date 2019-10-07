def toBinary(a):
    binaryA = ''
    while a > 0:
        binaryA = str(a % 2) + binaryA
        a = a // 2
    return binaryA

i = int(input('vvedite chislo dlia perevoda v dvoichnyy sistemy: '))
if i != 0:
    print(toBinary(i))
else:
    print('0 i est 0')