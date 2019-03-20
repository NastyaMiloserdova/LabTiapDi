from random import random
a = round(random()*100)
print("Требуется отгадать число, загаданное компьютером.")
b = int
while b != a:
  b = int(input())
  if b > a:
    print('Много. Попытайтесь еще.')
  elif b < a:
    print('Мало. Попытайтесь еще.')
  if b == a:
        print('Поздравляю! Вы угадали.')