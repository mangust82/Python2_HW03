# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

hike = {'палатка':2.5, 'спальник':1, 'коврик':0.4,'гермомешок':0.4, 'вода':2, 'еда':4, 'нож':0.2, 'скотч':0.2, 'спички':0.02, 'топор':1.2, 'средство от насекомых':0.2, 'powerbank':0.2, 'крем от загара':0.3, 'сапоги':1.1, 'толстовка':0.6 }

BACKPACK_WEIGHT = 10

general_weight = 0
for value in hike.values():
    general_weight += value

weigt_things = 0
list_things = []
for key, value in hike.items():
    weigt_things += value
    if weigt_things <= BACKPACK_WEIGHT:
        list_things.append(key)
    else:
        weigt_things -= value
print(f'Список вещей влезающих в рюкзак {list_things}')
print(f'Вес составил {weigt_things}')

# hike_list =[]
# for item in hike.items():
#     hike_list.append(item)
# print(hike_list)

# weigt_things = 0
# list_things = []
# list_list = [['a', 'ghj']]
# i = 0
# j = 0
# k = 0
# for i in range(len(hike_list)):
#     j = i + 1
#     for j in range(i + 1, len(hike_list)):
#         k = j
#         weigt_things = hike_list[i][1]
#         list_things.append(hike_list[i][0])
#         for k in range(j, len(hike_list)):
#             weigt_things += hike_list[k][1]
#             if weigt_things <= BACKPACK_WEIGHT:
#                 list_things.append(hike_list[k][0])
#             else:
#                 weigt_things -= hike_list[k][1]
#         if set(list_things) - set(list_list[j-1]):
#             list_list.append(list_things)
#             print(weigt_things, list_things)
#             weigt_things = 0
#             list_things.clear()
