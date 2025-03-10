# otazka_1
# čo sa vpíše na výstup, aké slovo alebo čislo
my_list = ["ano", "auto", 5, "tri", 9]
print(my_list[2])

# mám list
my_list = ["ano", "auto", 5, "tri", 9]
# Chcem na nultom mieste hodnotu 12
# Aby list vyzeral nasledovne:
[12, "auto", 5, "tri", 9]
# Aký príkaz musím použiť?

# append pridá na koniec listu to, čo je v zátvorkách
my_list = ["ano", "auto", 5, "tri", 9]
my_list.append("koniec")
print(my_list)
# Co sa vypíše na výstup ?


# len vypíše koľko vecí je v liste
my_list = ["ano", "auto", 5, "tri", 9]
print(len(my_list))
# Co sa vypíše na výstup ?


# Keď zadám prikaz:
print(my_list[2])
# vypíše na výstup:
# 5
# ktorý list musím vybrať aby to platilo


# Čo sa vypíše na konzolu?
cislo = 0
while cislo < 5:
    # end=' ' spôsobí, že sa po vypísaní hodnoty neprejde na nový riadok
    # bude sa stále vypisovať na jeden riadok a čísla budú oddelené medzerou
    print(cislo, end=" ")


# Čo sa vypíše na konzolu?
cislo = 0
while cislo < 5:
    # end=' ' spôsobí, že sa po vypísaní hodnoty neprejde na nový riadok
    # bude sa stále vypisovať na jeden riadok a čísla budú oddelené medzerou
    print(cislo, end=" ")
    cislo = cislo + 1


# Čo sa vypíše na konzolu?
my_list = ["p", "y", "t", "h", "o", "n"]
# len(my_list) zapíše do cislo koľko pismen je v my_list
cislo = 0
while cislo < len(my_list):
    # end=' ' spôsobí, že sa po vypísaní hodnoty neprejde na nový riadok
    # bude sa stále vypisovať na jeden riadok a písmená budú oddelené medzerou
    print(my_list[cislo], end=" ")
    cislo = cislo + 1


# Čo sa vypíše na konzolu?
my_list = [1, 2, 1, 2, 1, 2]
# len(my_list) zapíše do cislo koľko pismen je v my_list
cislo = 0
while cislo < len(my_list):
    # end=' ' spôsobí, že sa po vypísaní hodnoty neprejde na nový riadok
    # bude sa stále vypisovať na jeden riadok a slová budú oddelené medzerou
    if my_list[cislo] == 2:
        print("dva", end=" ")
    cislo = cislo + 1


a = 5
b = 3
# Aký výsledok vypíše na konzolu?
print(a + b)


# Čo sa vypíše na konzolu?
a = True
# Premennú a som nastavil na True
if a == True:
    print("Pravda")
else:
    print("Nepravda")


# Čo sa vypíše na konzolu?
for cislo in range(3):
    print(f"Číslo: {cislo}")
