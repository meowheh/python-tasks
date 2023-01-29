# Задание 1. Из строки «Python is the best programming language in the world» получить подстроку начиная с 6 символа
# с начала исходной строки и до 7 символа с конца исходной строки.

str = "Python is the best programming language in the world"
print(str[5:-7])

# Задание 2. Вывести каждый третий символа строки «Guido van Rossum is the benevolent dictator for life».

str = "Guido van Rossum is the benevolent dictator for life"
print(str[2::3])

#  Задание 3. Из строки «You have a problem with authority, Mr. Anderson.» получить словарь, где ключ - это символ,
#  а значение - это количество повторений символа в строке.

str = "You have a problem with authority, Mr. Anderson."
result = dict(zip(str, map(str.count, str)))
print(result)