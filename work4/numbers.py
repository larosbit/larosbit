# использование range()
for value in range(1,5):
       print(value)

for value in range(1,6):
       print(value)


# range отправляем в list

numbers = list(range(1,6))
print(numbers)

# построение четных чисел через 2
even_numbers = list(range(2,11,2))
print(even_numbers)

# возведение в квадрат чисел от 1 до 10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
# добавил git