# program zo zadaného slovného spojenia vytvorí akronym
# Spusti a ono sa opýta na slovné spojenie, ktoré potom na dva spôsoby prevedie na akronym
# Deti si skúsili vytvoriť akronym ako stringy, aj ako pole znakov

#as far as i know
#in my humble opinion
#By the way
#Away from keyboard

def main():
    # užívateľ zadá slová oddelené medzerou, ktoré sa hneď rozdelia na prvky poľa
    slovo  = input("Zadaj slovne spojenie: ").split(" ")
    # akronym bude zložený do jedného slova
    acronym = ''
    # akronym2 bude v skutočnosti prvky poľa, ktore sa nakoniec prevedie spojí do slova
    acronym2 = []    

    for word in slovo:
        # prechádzame každým slovom, ktoré zadal užívateľ a berieme z neho prvý znak
        # pridávame znak do akronymu
        acronym += word[0]
        acronym2.append(word[0])
    
    print("string sposob: " + acronym.upper())
    # prvky pola spojíme do stringu pomocou join a medzi jednotlivé prvky poľa sa vloží prázdny reťazec 
    acronym2 = "".join(acronym2)
    print("sposob pomocou poľa: " + acronym2.upper())

main()
