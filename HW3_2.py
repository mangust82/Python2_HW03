# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


NUMBER_OF_WORDS = 10

#ВВод текста с учетом перевода каретки 2 раза
text = ""
print('Введите текст: ')
while True:
    x = input()
    if x:
        text += x + " "
    else:
        break
print()

# формировоание списка из строки и сортировка
my_list = text.split()
N = len(my_list)
my_list.sort()

# формирование частотного словаря
my_dict = {}
for item in my_list:
    # my_list.count(item)
    my_dict.setdefault(item, my_list.count(item))
sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
i = 0

print(f'Количество слов в строке равно {N}')
print(f'{NUMBER_OF_WORDS} самых частых слов в тексте')

# Вывод 10 наиболее частых слов
for i in range(NUMBER_OF_WORDS):
    print(f'{i+1}. {sorted_dict[i][0]:>20} {sorted_dict[i][1]}')

# Вывод частотных слов длиной не менее 4 символов
# for item in sorted_dict:
#         if len(item[0]) >= 4 and i < 20:
#             print(f'{i+1}. {item[0]:>20} {item[1]}')
#             i += 1
#         elif i == 20:
#             break

