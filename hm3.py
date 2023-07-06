'''
eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

k = input('Введите слово на русском или английском языке: ')

if  k[0].lower() in eng:
    summa = 0
    for letter in  k:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f'стоимость введенного английского слова = {summa}')
else:
    if  k[0].lower() in rus:
        summa = 0
        for letter in  k:

            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f'стоимость введенного русского слова = {summa}')
'''

'''
import re
def isCyrillic( k):
	return bool(re.search('[а-яА-Я]',  k))
points_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
points_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
k = input('Введите слово').upper()
if isCyrillic( k):
	print(sum([k for i in  k for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in  k for k, v in points_en.items() if i in v]))
'''

'''
N = abs(int(input('Введите количество элементов в массиве: ')))
list_1 = input("Введите через пробел элементы массива: ").split()
num = list(map(int, list_1))
k = int(input('Введите число k, которое необходимо найти в массиве: '))
count = 0
for i in range(N):
    if num[i] == k:
        count += 1
print('Число k встречается: ->', count)
'''

# N = abs(int(input('Введите количество элементов массива: ')))
# list_1  = input("Введите через пробел элементы массива: ").split()
# num = list(map(int, list_1 ))
# k = int(input('Введите число k: '))
# min = abs(k - num[0])
# index = 0
# for i in range(1, N):
#     count = abs(k - num[i])
#     if count < min:
#         min = count
#         index = i
# print('Самый близкий по величине элемент к заданному числу k: -> ', num[index])


# list_2 = [1,2,3,1,1]
# l = 1
# result = list_2.count(l)
# print(result)

"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
"""

# list_1 = [1, 2, 3, 4,7]
# k = 6

# # Введите ваше решение ниже

# # num = list(map(int, list_]1 ))
# index = 0
# min = abs(k - list_1[0])
# for i in range(1, len(list_1)):
#     count = abs(k - list_1[i])
#     if count < min:
#         min = count
#         index = i
# print(list_1[index])

from functools import reduce


k = 'lizard'
score_list = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JXШЭЮ',
      	10:'QZФЩЪ'}
result =list(k)
list = list(k.upper())
sum = 0
for i in range(0,len(list)):
 for j in score_list:
  find = score_list[j].find(list[i])
  if find > -1 : sum += j
print(sum)
 