# задача "Удаление лищних пробелов"
strMy = input('Введите нескольк слов с любым количесвом пробелов: ')
normolizedRow = ''
tempRow = ''
import re
tempRow = re.findall('\w+',strMy)
for i in range(len(tempRow)): # складываем все слова
    normolizedRow += tempRow[i] + ' ' # склеиваем добавляя пробел
print(normolizedRow)