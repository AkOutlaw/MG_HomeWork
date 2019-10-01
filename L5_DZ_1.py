# задача "Самое длинное слово"
strMy = input('Vvedite neskolko slov cherez probel: ')
maxLengthWord = ''
import re
tempStr = re.findall('\w+',strMy) # получаем масив слов
for i in range(len(tempStr)): # перебираем, в переменную самое длинное
    if len(tempStr[i]) > len(maxLengthWord):
        maxLengthWord = tempStr[i]
print('The longest word is %s' % maxLengthWord, '\nThe lenght is %d' % len(maxLengthWord))