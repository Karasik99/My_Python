goroda = ['MG', 'minsk' , 'moscow' , 'sPB' , 'london']
print(goroda)
print(goroda[0])
print(goroda[1].title())
print(goroda[2].upper())
print(goroda[3].lower())
print(goroda[-1])
message = ('My favourite sity is ' + goroda[0].upper())
print(message)
print(goroda)
goroda[2] = 'OMSK'
print(goroda)
goroda.insert(2, 'Tomsk')
goroda.insert(0, 'Novgorod')
goroda.append('Brest')
print(goroda)
print('Теперь только два города')
my_sity = ['Novrorod', 'MG', 'minsk','Tomsk','OMSK','sPB','london','Brest']
first = my_sity.pop()
print(my_sity)
print(first)
second = my_sity.pop()
print(my_sity)
print(second)
third = my_sity.pop()
print(my_sity)
print(third)
fourth = my_sity.pop()
print(my_sity)
print(fourth)
print(my_sity)
del my_sity[1]
print(my_sity)
del my_sity[0]
print(my_sity)
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
goroda = ['mG', 'minsk' , 'moscow' , 'sPB' , 'london']
print(goroda)
goroda.sort()
print(goroda)
goroda.sort(reverse=True)
print(goroda)
print(sorted(goroda))
goroda.reverse
print(goroda)
