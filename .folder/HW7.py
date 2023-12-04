'''
Задача: print_operation_table
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
Пример
На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6 
3 6 9
'''

# Введите ваше решение ниже
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 :
        return print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    print(" ".join([str(k) for k in range(1, num_columns + 1)]))
    for i in range(2, num_rows + 1):
        s = " ".join([str(operation(i, j)) for j in range(2, num_columns + 1)])
        print(str(i) + " " + s)

print_operation_table(lambda x, y: x * y, 3, 3)

# Эталонное решение платформы:
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))


'''
Задача: Винни Пух
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.
Пример
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам пам-пам
'''

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# Введите ваше решение ниже
def check_rhythm(pooh_poetry):
    phrases = pooh_poetry.split()

    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    def count_syllables(word):
        vowels = "уеыаоэяиюУЕЫАОЭЯИЮ"
        return sum(1 for char in word if char in vowels)

    syllables_counts = [count_syllables(phrase.replace('-', '')) for phrase in phrases]

    if all(count == syllables_counts[0] for count in syllables_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

result = check_rhythm(stroka)
print(result)

# Эталонное решение платформы:
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#  print('Количество фраз должно быть больше одной!')
# else:
#  countVowels = []
#
#  for i in phrases:
#   countVowels.append(len([x for x in i if x.lower() in vowels]))
#
#  if countVowels.count(countVowels[0]) == len(countVowels):
#   print('Парам пам-пам')
#  else:
#   print('Пам парам')