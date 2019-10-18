
countOfProducts = int(input("Set total count of Products: "))

listOfProducts = [] # empty list for products

i = 1

for i in range(countOfProducts): # add products to list
    product = {} #
    product['id'] = i + 1
    product['name'] = input('Set product name: ')
    product['count'] = int(input('Set product count: '))
    product['price'] = int(input('Set product price: '))
    listOfProducts.append(product)
    print('Element is added!')
    print()

for i in range(len(listOfProducts)): # print added list of products
    print(listOfProducts[i])

print()

s = int(input('Set id of product to change! Set 0 to exit: '))   # item to change, if 0 exit
if s == 0:
    quit()

print()

tempProduct = listOfProducts[s-1]
tempProduct['count'] = int(input('Set new product count: '))
tempProduct['price'] = int(input('Set new price count: '))
listOfProducts.remove(listOfProducts[s-1])
listOfProducts.insert(s-1, tempProduct)

print('Here is updated list of products')
print()
for i in range(len(listOfProducts)):
    print(listOfProducts[i])

