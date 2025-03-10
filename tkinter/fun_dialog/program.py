# Toto bol veľmi obľúbený program a riešili sme ho niekoľko hodín
# Pôvodne mal program menšiu funkcionalitu, ale deti mali skvelé nápady, tak je to vylepšené

import tkinter as tk
import random

HEIGHT = 480
WIDTH = 480


def randfloat(left, right):
    return random.uniform(left, right)


def zobraz_odpoved():
    lbl_okno["text"] = "Vedel som to"


def posun_tlacitko(e):
    btn_nie.place(rely=randfloat(0.4, 0.9), relx=randfloat(0.4, 0.9))


def duplikuj_tlacitko(e):
    temp_btn = tk.Button(
        frm_main, text="zduplikuj", bg="yellow", relief=tk.RAISED, borderwidth=3
    )
    temp_btn.place(rely=randfloat(0.1, 0.9), relx=randfloat(0.1, 0.9))
    temp_btn.bind("<Enter>", duplikuj_tlacitko)


def clk_tmp(e):
    lbl_okno["text"] = "Pretože nevie učiť"


main_window = tk.Tk()
frm_main = tk.Frame(main_window, height=HEIGHT, width=WIDTH)
frm_main.pack()

lbl_okno = tk.Label(frm_main, bg="white", font=("Courier", 15), justify="center")
lbl_okno.place(relx=0.2, rely=0.2, relheight=0.2, relwidth=0.6)
lbl_okno["text"] = "Si debil?"

btn_ano = tk.Button(
    frm_main,
    text="ano",
    bg="green",
    relief=tk.RAISED,
    borderwidth=3,
    command=lambda: zobraz_odpoved(),
)
btn_ano.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.2)

btn_nie = tk.Button(
    frm_main,
    text="nie",
    bg="red",
    relief=tk.RAISED,
    borderwidth=3,
)
btn_nie.place(relx=0.6, rely=0.6, relheight=0.1, relwidth=0.2)
btn_nie.bind("<Enter>", posun_tlacitko)

btn_3 = tk.Button(
    frm_main, text="učitel tiež", bg="blue", relief=tk.RAISED, borderwidth=3
)
btn_3.place(relx=0.6, rely=0.8, relheight=0.1, relwidth=0.2)

btn_3.bind("<Button>", clk_tmp)

btn_4 = tk.Button(
    frm_main, text="zduplikuj", bg="yellow", relief=tk.RAISED, borderwidth=3
)
btn_4.place(relx=0.1, rely=0.8, relheight=0.1, relwidth=0.2)

btn_4.bind("<Enter>", duplikuj_tlacitko)

main_window.mainloop()
