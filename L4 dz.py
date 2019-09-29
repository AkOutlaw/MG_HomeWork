cont = 'yes'
while cont.lower() != 'no':
    print('Ravmobedreniy treygolnic!!!\n')
    height = int(input('Vvedite visoty treygolnika: '))
    for i in range(0, height):
        i += 1
        for j in range(1, height - i + 1): # рисуем отступы
            print(' ', end='')
            j += 1
        for j in range(height - (2 * i) + 1, height): # рисуем ^
            print('^', end='')
            j += 1
        print('')
    cont = input('Hotite prodolzat? Type yes or no ')