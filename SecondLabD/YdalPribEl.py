el = int(input('Введите желаемое количество элементов :) '))
if el <= 10:
    print('Настоятельно прошу ввести больше десяти элементов :Р ')
    el = int(input())
m = []
for i in range(0, el):
    m.append(int(input('Введите' + '   ' + str(i+1) + '   ' + "элемент списка - ")))
print(m)
del_idx = {0, 1}
m[:] = [x for i, x in enumerate(m) if i not in del_idx]
print(m)
for i in range(2):
 m.append(int(input('Введите новый ' + '   ' + str(i+1) + '   ' + "элемент списка - ")))
print(m)