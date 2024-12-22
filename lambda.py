# LAMBDA
# add
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
add = lambda a,b: a + b
print(add(x,y))

# substration
substration= lambda a,b: a - b
print(substration(x,y))

# multiplicacion
multiplication = lambda a,b: a * b
print(multiplication(x,y))

# division
division = lambda a,b: a / b
print(division(x,y))


# lambda-filter
num = [1,2,3,4,5,6,7,8,9,10]
num_2 = [4,5,2,1,3,9,0,7,10,6]

squared = filter(lambda x: x % 2 != 0, num)
print(list(squared))

ordered = sorted(num_2)
print(list(ordered))
print(list(filter(lambda x: x % 3 == 0, ordered)))
