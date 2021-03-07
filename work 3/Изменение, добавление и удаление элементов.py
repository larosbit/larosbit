motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)


# разделение
print("__________________________________")
# добавление в коенц массива метод .append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


# разделение
print("__________________________________")

# .append  c пустым списком
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# разделение
print("__________________________________")


# метод insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)


# разделение
print("__________________________________")


# удаление , команда del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[2]
print(motorcycles)

# разделение
print("__________________________________")

# удаление элемента с сохранением в переменной , метод pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)



# разделение
print("__________________________________")


# какой мотоцикл купили последним , метод .pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


# разделение
print("__________________________________")


# выделение позиции из массива в переменную, с дальнейшим применением. используется метод .pop()
# После какждого вызова .рор() элемент не находится в списке
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() +'.')




# разделение
print("__________________________________")


# удаление элементов по значениюё, метод .remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

