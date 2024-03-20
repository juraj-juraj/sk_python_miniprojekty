import tkinter as tk
import random

window = tk.Tk()
# Definujeme si hlavné okno o veľkosti 400x400
main_frame = tk.Frame(window, height=400, width=400)
main_frame.pack()

# Vytvoríme label s textom "Si blbý?" a nastavíme mu farbu pozadia a veľkosť písma
# Label sa umiestni na dané miesto v okne, relx a rely sú relatívne súradnice, kde 0 je v ľavom hornom rohu a 1 je v pravom dolnom
# relief a borderwidth sú nastavenia okraja labelu. tk.RAISED znaméná, že okraj bude vypuklý a borderwidth je veľkosť okraja.
text_label = tk.Label(text="Si blbý?", bg="#f095da", relief=tk.RAISED, borderwidth=10)
# Umiestnime label dostredu, v hornej tretine okna, s veľkosťou 60% šírky a 20% výšky
text_label.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)


# Funkcia náhodne presunie tlačitko, ktoré ho spustí
def nie_action(e):
    # vygenerujeme náhodné čislo medzi 0 a 1, pre nové umiestnenie daného widgetu
    nahodne_y = random.randrange(0, 85) / 100
    nahodne_x = random.randrange(0, 80) / 100
    # e.widget je v tomto prípade button, ktorý spustil túto funkciu
    # Umiestnime widget na nové náhodné miesto
    e.widget.place(relx=nahodne_x, rely=nahodne_y)


def ano_button_action(e):
    """
    Zmeníme text labelu na "vedel som to"
    Label je ten, ktorý je nadefinovaný vyššie
    text_label je globálna premenná, ktorú môžeme meniť kdekoľvek
    text_label obsahuje slovník, dictionary, kde môžeme meniť rôzne vlastnosti labelu
    Teraz meníme text, preto je v hranatých zátvorkách "text", na "vedel som to"
    """
    text_label["text"] = "vedel som to"


def ano_enter_action(e):
    """
    Funkcia, ktorá vygeneruje nové tlačitko "ano" na náhodnom mieste a priradí mu vlastnosti:
        - text na ano, oranžová farba, veľkosť písma 15, veľkosť tlačítka 15x15
        - bind na funkciu ano_button_action, na kliknutie, ktorá zmení text labelu, pozri funkciu ano_button_action
        - bind na funkciu ano_enter_action, na prechod, ktorá vygeneruje nové tlačitko "ano"
    """
    ano_button = tk.Button(
        text="ano", font=("Courier", 15), padx=15, pady=15, bg="#de4816"
    )
    # Ak kliknem na tlacidlo, spusti sa funkcia ano_button_action, zmeni sa text labelu
    ano_button.bind("<Button>", ano_button_action)
    # Ak prejdem myšou nad tlačítko, vygeneruje sa nové tlačítko "ano"
    ano_button.bind("<Enter>", ano_enter_action)
    # Nové tlačítko umiestnime na náhodné miesto
    nahodne_y = random.randrange(0, 85) / 100
    nahodne_x = random.randrange(0, 80) / 100
    ano_button.place(relx=nahodne_x, rely=nahodne_y)


# Vytvárame tlačitko "nie" s textom "nie", veľkosťou písma 20, veľkosťou tlačítka 20x20 a farbou pozadia #95f0e1
nie_button = tk.Button(text="nie", font=("Courier", 20), padx=20, pady=20, bg="#95f0e1")
# Ak prejdem myšou nad tlacidlo, spusti sa funkcia nie_action, presunie sa tlačítko "nie" na náhodné miesto
nie_button.bind("<Enter>", nie_action)
# Umiestnime tlačítko na 75% šírky a 75% výšky okna, teda v pravom dolnom rohu. Aspoň zo začiatku tu bude
nie_button.place(relx=0.75, rely=0.75)

# Tlačitko "ano" s textom "ano", veľkosťou písma 20, veľkosťou tlačítka 20x20 a farbou pozadia #de4816
ano_button = tk.Button(text="ano", font=("Courier", 20), padx=20, pady=20, bg="#de4816")
# Ak kliknem na tlacidlo, spusti sa funkcia ano_button_action, zmeni sa text v text_label na vedel som to
ano_button.bind("<Button>", ano_button_action)
# Ak prejdem myšou nad tlačítko, vygeneruje sa nové tlačítko "ano" na náhodnom mieste
ano_button.bind("<Enter>", ano_enter_action)
ano_button.place(relx=0.10, rely=0.75)

window.mainloop()
