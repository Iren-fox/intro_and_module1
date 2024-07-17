immutable_var=tuple([1, 2, 3, 'привет', True])
print('Immutable_var: ',immutable_var)
#immutable_var[2]=555 
#print(immutable_var) #на выходе ошибка, т.к. менять элементы кортежа нельзя
mutable_list=['понедельник', 'среда', 'пятница', 1, 2, 25]
print('Mutable_list: ',mutable_list)
mutable_list[0]='воскресенье'
print('Mutable_list измененный: ',mutable_list)
mutable_list.append(False)
print('Mutable_list измененный_2: ',mutable_list)