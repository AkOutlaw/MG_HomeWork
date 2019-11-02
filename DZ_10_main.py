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


maxS = 0
maxP = 0

maxSType = ''
maxPType = ''

for i in figuresList:
    s = i.getSquare()

    p = i.getPerimeter()

    if maxS < s:
        maxS = s
        maxSType = i.getName()
    if maxP < p:
        maxP = p
        maxPType = i.getName()

choice2 = input('Select parameter for calculation: Square(s) or Perimeter(p): ')

if choice2 == 's':
    print('Max square is %4s; figure: %4s' % (maxS, maxPType))
elif choice2 == 'p':
    print('Max Perometer is %4s; figure: %4s' % (maxP, maxPType))
else:
    print('invalid input \n')
    print('Max square is %4s; figure: %4s' % (maxS, maxPType))
    print('Max Perometer is %4s; figure: %4s' % (maxP, maxPType))
