# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

#num_list = [2, 3, 2, 5, 2, 8]
#word_list = ["hello", "one", "two", "one", "three"]

num = input("Enter the number: ")
num_s_l = [str(num_l) for num_l in num_list]
num_s = " " + " ".join(num_s_l) + " "

#print(num_s)
str_index = num_s.rfind(" " + num + " ")
#print(str_index)
index = num_s[:str_index].count(" ")
#print(num_s[:str_index])
#print(index)
print("Index of the latest match of {0} is {1}.".format(num, str(index)))




word = input("Enter the word: ")
word_s = " " + " ".join(word_list) + " "
str_index = word_s.rfind(" " + word + " ")
index = word_s[:str_index].count(" ")
print("Index of the latest match of {0} is {1}.".format(word, str(index)))

