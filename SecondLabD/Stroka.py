str1 = 'Дана строка, состоящая из слов, пробелов и знаков препинания.'
str2 = str1.split()
f = 0
while f < len(str2):
 str2[f] = str2[f].replace(',', ' ')
 str2[f] = str2[f].replace('.', ' ')
 str2[f] = str2[f].replace('—', ' ')
 str2[f] = str2[f].replace('!', ' ')
 str2[f] = str2[f].replace('?', ' ')
 f += 1
str1 = ''
for elem in str2:
 if len(elem) > 5:
  str1 +=  elem + ' - '
print(str1)