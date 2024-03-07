# Python prehľad


# Základné dátové typy, s ktorými budeme narábať: str, int, float list, dict, tuple, bool, None
# str - slová, texty, sú v úvodzovkách napr: "slovo"
# int - celé čísla, napr: 5, 7
# float - desatinné čísla, napr: 3.14, 2.5
# dict - slovník, zoznam hodnôt, ktoré sú priradené k unikátnym kľúčom, napr: {"meno": "John", "vek": 25}
# list - zoznam hodnôt, ktoré môžu byť rôznych typov a majú indexy, napr: [1, "hello", True]
# tuple - usporiadaná nezmeniteľná sekvencia hodnôt, napr: (1, 2, 3)
# bool - logická hodnota True alebo False, napr: True, False
# None - špeciálna hodnota, ktorá reprezentuje neprítomnosť hodnoty, napr: None

# List

my_list = [1, 2, 3, 4]

print(my_list)
# [1, 2, 3, 4]

print(my_list[0])
# 1

# Len ako length, vypíše koľko prvkov má list
print(len(my_list))
# 4

my_list.append(7)
print(my_list)
# [1,2,3,4,7]

my_list = [1, 2, 3, 4]

print(my_list * 2)
# [1, 2, 3, 4, 1, 2, 3, 4]
# Toto použivame napriklad ak chceme list s rovnakými prvkami a  nejakej dĺžky
a = [0] * 5
print(a)
# [0, 0, 0, 0, 0]

my_list_2 = [8, 9]
print(my_list + my_list_2)
# [1, 2, 3, 4, 8, 9]

# Môžeme vyberať celé časti listov
# Fancy indexing
# Do hranatých zátvoriek dáme indexy [od:do]
# od - je vrátane
# do - prvok s tým indexom už nerátame
# Ak vynecháme jeden koniec intervalu, automaticky sa berie do daného konca
my_list_3 = [1, 2, 3, 4, 5, 6, 7]
print(my_list[1:3])
# [2,3]
print(my_list[:4])
# [1,2,3,4]

## Dictionaries
my_dict = {"name": "John", "age": 25, "city": "New York"}

print(my_dict)
# {'name': 'John', 'age': 25, 'city': 'New York'}

print(my_dict["name"])
# John

# Len ako length, vypíše koľko prvkov má slovník
print(len(my_dict))
# 3

# Môžeme vyberať hodnoty podľa kľúča
print(my_dict["city"])
# New York

my_dict["age"] = 30
print(my_dict)
# {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict["occupation"] = "Engineer"
print(my_dict)
# {'name': 'John', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}

# Môžeme vyberať všetky kľúče
print(my_dict.keys())
# dict_keys(['name', 'age', 'city', 'occupation'])

# Môžeme vyberať všetky hodnoty
print(my_dict.values())
# dict_values(['John', 30, 'New York', 'Engineer'])

# Môžeme vyberať všetky páry kľúč-hodnota
print(my_dict.items())
# dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('occupation', 'Engineer')])


## Funkcie


# Jednoduché funkcie
# Sčíta dve čisla a vráti ich výsledok
def sum_numbers(a, b):
    return a + b


def print_hey():
    print("hey")


# Duck typing
# O každom argumente funkcie hovoríme akého dátového typu bude
# a:int znamená, argument a je typu int, celé číslo
# -> int znamená že návratová hodnota tejto funkcie je int, celé čislo
def sum_numbers_typed(a: int, b: int) -> int:
    return a + b


# Argumenty s východzou hodnotou
# argument b môžeme zadať ako normálny druhý argument
# Ak b nezadáme, nemusíme, tak bude mať hodnotu 1
def sum_numbers_default(a: int, b: int = 1) -> int:
    return a + b


# Nezadali sme druhý parameter, ale má defaultnú hodnotu 1. Preto bude súčet 3
print(sum_numbers_default(a=2))
# 3


## Cykly

# for prechádza cez prvky objektu
# Postupne berie po jednom prvok po prvku a vkladá ich do `i`
for i in range(3):
    print(i)
# 0
# 1
# 2

for i in ["a", "b", "c"]:
    print(i)
# a
# b
# c

# While prechádza cyklus dokým je podmienka pravdivá
# Potom z cyklu vystúpi a program pokračuje ďalej
i = 4
while i > 0:
    print(i)
    i = i - 1
# 4
# 3
# 2
# 1
