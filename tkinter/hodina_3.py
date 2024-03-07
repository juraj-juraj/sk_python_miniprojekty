import tkinter as tk
import random

# Program z prvej časti hodiny,
# Zobrazí dva nápisy a dve tlačitka
# Použitie pack() metody
#
# window = tk.Tk()
# label = tk.Label(text="toto funguje", bg="#03fc0b", fg="#b81a59")
# # Fill=x zabezpečí, že label sa roztiahne na celú širku okna, nech je hocijako veľké
# label.pack(fill="x")

# # Padx a pady je v podstate veľkosť krajov okolo textu. Uvidíte, podľa toho kam až siaha modré pozadie
# label = tk.Label(text="tento je druhy", padx=100, pady=20, bg="blue", fg="#b81a59")
# label.pack()


# def button_1_action(e):
#     # e je objekt eventu, udalosti, ktorý sa stal obsahuje dáta o tom, čo bolo spustené a na akom objekte sa to stalo
#     # e.widget je objekt buttonu, ktorý bol stlačený
#     # Zmeníme farbu pozadia na danom tlačítku
#     e.widget["bg"] = "#b8931a"


# button_1 = tk.Button(text="vypni program", font=("Courier", 20))
# # Pri stlačení button_1, stlačenie je "<Button>", sa spustí funkcia button_1_action
# button_1.bind("<Button>", button_1_action)
# button_1.pack()

# button_2 = tk.Button(text="druhe tlacitko", font=("Courier", 20))
# # <Enter> znamená, že stači len prejsť myšou nad tlačítko
# button_2.bind("<Enter>", button_1_action)
# button_2.pack()


window = tk.Tk()
# Definujeme si hlavné okno o veľkosti 400x400
main_frame = tk.Frame(window, height=400, width=400)
main_frame.pack()

si_blby = tk.Label(text="Si blbý", bg="#f095da", relief=tk.RAISED, borderwidth=10)
si_blby.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)


# Funkcia náhodne presunie tlačitko, ktoré ho spustí
def ano_action(e):
    # vygenerujeme náhodné čislo medzi 0 a 1, pre nové umiestnenie daného widgetu
    nahodne_y = random.randrange(0, 100) / 100
    nahodne_x = random.randrange(0, 100) / 100
    # Umiestnime widget na nové náhodné miesto
    e.widget.place(relx=nahodne_x, rely=nahodne_y)


ano_button = tk.Button(text="ano", font=("Courier", 20), padx=20, pady=20, bg="#95f0e1")
ano_button.bind("<Enter>", ano_action)
ano_button.place(relx=0.75, rely=0.75)

window.mainloop()
