numbtr = 3
number = 4
number2 = 5
result = numbtr +number2
print (result)

num1 = num2 = 5
print (num1, num2)

num_1, num_2 = 5,7
print(num_1, num_2)

# Меняет местами
swap1 = 6
swap2 = 9
swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2)

swap2 -= number
print(swap2)

# Распаковка списка по переменной
z, *x, c = [1, 2, 3, 4, 5]
print (z)
print (x)
print (c)


numb1 = int(input('Введите 1 число: '))
numb2 = int(input('Введите 2 число: '))

print('Result: ', numb1 + numb2)
print('Result: ', numb1 - numb2)
print('Result: ', numb1 * numb2)
print('Result: ', numb1 / numb2)
