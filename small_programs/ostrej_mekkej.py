# Program inšpirovaný filmom The Simpsons
# Na pripomenutie scéna z filmu: https://www.youtube.com/watch?v=sN7K5bn7rB4  ostrej mekkej
# Program náhodne generuje zoradenie vojakov  

from random import randrange

# povieme si akých typov máme vojakov
soldier_type = ["ostrej", "mekkej"]

# zjednodušená implementácia, keď zadáme iba koľko máme vojakov a ono to nageneruje rozloženie
def soldiers_total():
    count = int(input("zadaj pocet vojakov: "))
    for i in range(count):
        # randrange nám náhodne vyberá index do poľa soldier type, podľa toho sa vypíše ostrej alebo mekkej
        print(soldier_type[randrange(0, len(soldier_type))])

# vylepšená implementácia, ked konkrétne zadáme koľko máme akých vojakov
def soldiers_type():
    # s_count je pole koľko je akých vojakov, na začiatku dáme, že oboch skupín je 0
    s_count = {0, 0}
    s_count[0] = int(input("zadaj pocet ostrych: "))
    s_count[1] = int(input("zadaj pocet mekkych: "))

    for i in range(sum(s_count)):
        # ak už som vyčerpal vojakov z nejakej skupiny, tak nemusím použivať randrange,
        # rovno len budem už vypisovať len z tej skupiny, kde este ostali nezaradení vojaci
        if(s_count[0] == 0 or s_count[1] == 0):
            if(s_count[0] != 0):
                print(soldier_type[0])
            else:
                print(soldier_type[1])
        else:
            index = randrange(0, len(soldier_type))
            print(soldier_type[index])
            # odpočitam z tej skupiny vojakov jedného, pretože sa práve použil 
            s_count[index] -= 1

# teraz zavolám soldiers_total(), pre zjednodušenú implementáciu alebo soldiers_type() pre zložitejší algoritmus
soldier_type()
soldiers_total()

