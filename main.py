# homework 'circle'
pi = 3.1415926
radius = 42
space = pi * (radius ** 2)
space = round(space, 4)

print('Площадь круга:', space)

point_1 = (23, 34)
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** .5

print('Расстояние от нуля до точки:', distance_1)

if distance_1 <= radius:
    print('True')
else:
    print('False')

point_2 = (30, 30)
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** .5

print('Расстояние от нуля до точки:', distance_2)

if distance_2 <= radius:
    print('True')
else:
    print('False')

# homework 'operations'
number = ((1 + 2) * 3 - 4) * 5
print(number)

# homework 'favorite_moves'

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

print(my_favorite_movies[0:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])

# homework my family

my_family = ['mother', 'father', 'sister', 'brother']

my_family_height = [
    ['father', 173],
    ['mother', 165],
    ['sister', 155],
    ['brother', 182]
]

print('Рост', my_family[1], '-', my_family_height[0][1], 'см')

sum_height = 0
sum_height += my_family_height[0][1]
sum_height += my_family_height[1][1]
sum_height += my_family_height[2][1]
sum_height += my_family_height[3][1]

print('Общий рост моей семьи -', sum_height, 'см.')

# homework zoo

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]

zoo.insert(1, 'bear')
zoo.extend(birds)
zoo.remove(zoo[3])
print(zoo)
print('lion in', zoo.index('lion')+1)
print('lark in', zoo.index('lark')+1)

# homework songs list

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

sum_sound_time = 0
sum_sound_time += violator_songs_list[3][1]
sum_sound_time += violator_songs_list[5][1]
sum_sound_time += violator_songs_list[8][1]

print('три песни играют:', sum_sound_time, 'минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


sum_sound_time_2 = 0
sum_sound_time_2 += violator_songs_dict['Sweetest Perfection']
sum_sound_time_2 += violator_songs_dict['Policy of Truth']
sum_sound_time_2 += violator_songs_dict['Blue Dress']

print('а другие три песни играют:', sum_sound_time_2, 'минут')

# homework secret

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

print(secret_message[0][3])
print(secret_message[1][9:13])
print(secret_message[2][5:15:2])
print(secret_message[3][12:6:-1])
print(secret_message[4][20:15:-1])

# homework garden

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set.union(meadow_set))
print(garden_set & meadow_set)
print(garden_set.difference(meadow_set))
print(meadow_set.difference(garden_set))

# homework shopping

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99}
    ],
    'конфеты': [
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ]
}

print(sweets)

# homework store

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_quantity = sofas_item['quantity']
sofas_price = sofas_item['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
