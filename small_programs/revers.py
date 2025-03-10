# Program písmenko po písmenku otočí zadané slovo
# Algoritmus je robený in site, slovo otáča priamo v zadanom reťazci

def main():
    slovo = list(input("zadaj slovo: "))
    temp = ''
    w_len = len(slovo)
    # prechádzame len do polovice slova a vymieňame hlásky s hláskou na opačnom konci slova
    # musíme použiť celočiselné delenie, aby sa stredná hláska pri párnej dĺžke nemenila sama so sebou
    for i in range(w_len//2):
        temp = slovo[i]
        slovo[i] = slovo[w_len - i -1]
        slovo[w_len - i - 1] = temp
    print("obratene slovo: ", ''.join(slovo))
main()
