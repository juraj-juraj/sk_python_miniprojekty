# Program vykresluje v terminali funkcie
# Vykresluje otocene o 90 stupnov 
# Pre deti, ktoré ešte nepreberali funckie v škole to bolo trocha náročné

import math

# Toto vykresluje kopce ako funkciu 
#
##
###
####
#####
####
###
##
#

#
##
###
####
#####
####
###
##
#



def jednoducha_funkcia(x):
    return x**2+4

def sinusova_funkcia(x):
    return round((math.sin(math.pi * x / 5) + 1) * 10)+2

def kopcova_funkcia(x):
    return round(((x%5)**2))+1

def funkcia_kopcova():
    pocet_kopcov = int(input("Kolko period ma ubehnut: "))
    zadana_vyska = int(input("Zadaj maximalnu vysku kopcov: "))
    print('')
    while(pocet_kopcov > 0):
        perioda = 0
        # najprv vystupa do výšky
        while(perioda <= zadana_vyska):
            perioda += 1
            print('#'*(perioda))
        
        # Potom sklesá
        while(perioda > 0):
            print('#' * perioda)
            perioda -= 1
        pocet_kopcov -= 1

# Vykresluje funkcie z pribalenej knižnice
# Sú tam jednoduché kvadratické funkcie

def funkce_parametricka():
    dolna_medz = int(input("Zadaj zaciatok pocitania: "))
    horna_medz = int(input("Zadaj do kolko pocita: "))
    # Index je funkčná hodnota, začina sa počitať pre dolnú medz a počita sa až do dolnej medze
    index = dolna_medz
    funkcna_hodnota = 0
    integral = 0
    while(index < horna_medz):
        # Tuto sa dajú vybrať funkcie, ktoré sa budú vykreslovať
        # Tie matematicke funkcie maju ako vstup x a vracajú y
        funkcna_hodnota = jednoducha_funkcia(index)
        #funkcna_hodnota = kopcova_funkcia(index)
        #funkcna_hodnota = sinusova_funkcia(index)
        integral += funkcna_hodnota
        print('#' * int(funkcna_hodnota))
        index += 1
    print("Integral od {} do {} je {}".format(dolna_medz, horna_medz, integral))
    
#funkcia_kopcova()
funkce_parametricka()

    
