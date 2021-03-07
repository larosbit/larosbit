# 3-4 список гостей и приглешение на обед
guest = ['Liza', 'Roma', 'Rich', 'Dasha']
invite = (" welcome to lunch!")
print(guest)
print(guest[0]+","+invite)
print(guest[1]+","+invite)
print(guest[2]+","+invite)
print(guest[3]+","+invite)
# доп задание, один гость не придет
print(guest[3]+","+" won't come for lunch.")
# 3-5 список с удалением и добавлением гостя
del guest[3]
guest.append('Masha')
print(guest)
invite = (" welcome to lunch!")
print(guest[0]+","+invite)
print(guest[1]+","+invite)
print(guest[2]+","+invite)
print(guest[3]+","+invite)
# доп задание
print("Added places for guest")
# 3-6 добавление людей в список
guest.insert(0, 'Sasha')
guest.insert(2, 'Kate')
guest.append('Sofa')
print(guest)
print(guest[0]+","+invite)
print(guest[1]+","+invite)
print(guest[2]+","+invite)
print(guest[3]+","+invite)
print(guest[4]+","+invite)
print(guest[5]+","+invite)
print(guest[6]+","+invite)
# 3-7 Сокращение гостей + извинение за ложное приглашение
guest = ['Sasha', 'Liza', 'Kate', 'Roma', 'Rich', 'Masha', 'Sofa']
print("Only two people can come to lunch")
popped_guest = guest.pop()
print(popped_guest+","+" Sorry my dear friend, but places only two, I cannot invite you;(")
popped_guest = guest.pop()
print(popped_guest+","+" Sorry my dear friend, but places only two, I cannot invite you;(")
popped_guest = guest.pop()
print(popped_guest+","+" Sorry my dear friend, but places only two, I cannot invite you;(")
popped_guest = guest.pop()
print(popped_guest+","+" Sorry my dear friend, but places only two, I cannot invite you;(")
popped_guest = guest.pop()
print(popped_guest+","+" Sorry my dear friend, but places only two, I cannot invite you;(")
# подтверждение приглашения для двух гостей
message = (" dear friend, my invite for you is still valid.")
print(guest[0]+","+message)
print(guest[1]+","+message)
# удаление из списка оставшихся двоих
del guest[0]
del guest[0]
print(guest)