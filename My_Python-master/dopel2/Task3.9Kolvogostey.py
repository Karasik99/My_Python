my_guests = ['Egor', 'Lesha', 'Sasha']
print(my_guests)
print('Hello ' + my_guests[0] + ' go drink a beer !!')
print('Hello ' + my_guests[1] + ' go drink a beer !!')
print('Hello ' + my_guests[2] + ' go drink a beer !!')
print('Sasha ne smog priiti tak kak on ymer')
my_guests[2] = 'Oleg'
print(my_guests)
print('Hello ' + my_guests[0] + ' go drink a beer !!')
print('Hello ' + my_guests[1] + ' go drink a beer !!')
print('Hello ' + my_guests[2] + ' go drink a beer !!')
my_guests.insert(2, 'Slava')
my_guests.insert(0, 'Alesya')
my_guests.append('Andrey')
print(my_guests)
print('Hello ' + my_guests[0] + ' go drink a beer !!!')
print('Hello ' + my_guests[1] + ' go drink a beer !!!')
print('Hello ' + my_guests[2] + ' go drink a beer !!!')
print('Hello ' + my_guests[3] + ' go drink a beer !!!')
print('Hello ' + my_guests[4] + ' go drink a beer !!!')
print('Hello ' + my_guests[5] + ' go drink a beer !!!')
print('Теперь только два гостя')
my_people = ['Alesya', 'Egor', 'Lesha','Slava','Oleg','Andrey']
len(my_people)
first = my_people.pop()
print('Пока Андрей')
print(my_people)
print(first)
print('Пока Олег')
second = my_people.pop()
print(my_people)
print(second)
print('Пока Слава')
third = my_people.pop()
print(my_people)
print(third)
print('Пока Леха')
fourth = my_people.pop()
print(my_people)
print(fourth)
print('Алеся и Егор ваши приглашения остаются в силе')
print(my_people)
del my_people[1]
print(my_people)
del my_people[0]
print(my_people)
print(len(my_guests))
print(len(my_people))