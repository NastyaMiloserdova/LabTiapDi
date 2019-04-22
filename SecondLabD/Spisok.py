my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_' \
            'Петров;Семен;Игоревич;22 года;Студент 2 курса'
my_list = my_string.split(';')
print(my_list)
f = 0
my_list1 = my_string.split('_')
while f < len(my_list1):
 my_list1[f] = my_list1[f].replace(';', ' ')
 f += 1
print("%39s" % (my_list1[0]))
my_list1.pop(0)
for i in range(len(my_list1)):
 print("%0s" % (my_list1[i]))