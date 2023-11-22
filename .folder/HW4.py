"""
Задача: Пересечение двух неупорядоченных наборов целых чисел
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
Пример
На входе:
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:
3 5
"""

var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

def common_nums(n, m, set1, set2):
    set1 = set(map(int, set1.split()))
    set2 = set(map(int, set2.split()))
    common = set1.intersection(set2)
    result = ' '.join(sorted(map(str, common)))
    return result

n, m = map(int, var1.split())
common = common_nums(n, m, var2, var3)
print(common)

# эталонное решение платформы:
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')


"""
Задача: Черника
В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.
В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.
Входные данные:
На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
Выходные данные:
Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
Пример использования 
На входе:
arr = [5, 8, 6, 4, 9, 2, 7, 3]
На выходе:
19
"""


arr = [5, 8, 6, 4, 9, 2, 7, 3]

def max_berry_collection(arr):
    n = len(arr)
    total_berries = [0] * n
    for i in range(n):
        total_berries[i] = arr[i] + arr[(i - 1) % n] + arr[(i - 2) % n]
    max_berries = max(total_berries)
    return max_berries

max_berries = max_berry_collection(arr)
print(max_berries)

# эталонное решение платформы:
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# # Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))