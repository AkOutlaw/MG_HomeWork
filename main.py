import figures

figuresList = []

for i in range(3):
    choice = input("Круг(к), прямоугольник(п) или треугольник(т): ")

    if choice == 'к':
        figure = figures.Circle(float(input("Радиус: ")))

    elif choice == 'п':
        l = float(input("Длина: "))
        w = float(input("Ширина: "))

        figure = figures.Rectangle(w, l)

    elif choice == 'т':
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        c = float(input("Третья сторона: "))

        figure = figures.Triangle(a, b, c)

    figuresList.append(figure)

choice2 = input('Which parameter will be calculated: perimeter(p) or square(s): ')


maxS = 0
maxP = 0

listSquares = []
listPerimeters = []

vocSq = {}
vocPer = {}

for i in figuresList:
    s = i.getSquare()
    vocSq[i] = s
    listSquares.append(vocSq)

    p = i.getPerimeter()
    vocPer[i] = p
    listPerimeters.append(vocPer)

    if maxS < s:
        maxS = s
        figWithMaxSquare = i
    if maxP < p:
        maxP = p
        figWithMaxPerimeter = i

choice3 = input('Input number of figure')
print(listSquares)
print(listPerimeters)
# if choice2 == 's':
#     print('Square is %4s; figure: %4s' % (maxS, type(figWithMaxSquare)))
# elif choice2 == 'p':
#     print('Square is %4s; figure: %4s' % (maxP, type(figWithMaxPerimeter)))

