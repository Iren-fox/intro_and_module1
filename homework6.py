my_dict={'Иванов':5, 'Волков':3, 'Смирнов':4, 'Антонов':2}
print(my_dict)
print(my_dict['Волков'])
my_dict['Сидоров']=5
print(my_dict['Сидоров'])
my_dict.update({'Соколов':4,
								'Морозов':3})
print(my_dict)
a=my_dict.pop('Антонов')
print(a)
print(my_dict)
my_set={'понедельник', 'вторник','понедельник'}
print(my_set)
my_set.update({False, 123})
print(my_set)
my_set.remove(False)
print(my_set)