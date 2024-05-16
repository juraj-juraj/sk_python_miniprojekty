import tkinter as tk


def cipher_button_action(event):
    text = input_text.get("1.0", tk.END)
    ord_text = []
    for char in text:
        ord_text.append(ord(char))

    for i in range(len(ord_text)):
        ord_text[i] = ord_text[i] + 1

    characters = []
    for number in ord_text:
        characters.append(chr(number))

    sifrovany_text = "".join(characters)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, sifrovany_text[: len(sifrovany_text) - 1])


main_window = tk.Tk()
main_window.title("Cipher program")

main_frame = tk.Frame(master=main_window, height=400, width=400)
main_frame.pack()

control_frame = tk.Frame(master=main_frame)
input_label = tk.Label(master=control_frame, text="Zadaj text")
input_label.grid(row=0, column=0)
cipher_button = tk.Button(master=control_frame, text="Zasifruj")
cipher_button.grid(row=0, column=1, padx=100)
cipher_button.bind("<Button>", cipher_button_action)
decipher_button = tk.Button(master=control_frame, text="Odsifruj")
decipher_button.grid(row=0, column=2)

control_frame.grid(row=0, column=0)

input_frame = tk.Frame(
    master=main_frame, padx=10, pady=10, borderwidth=2, relief=tk.RAISED
)
input_text = tk.Text(master=input_frame, height=10)
input_text.pack()
input_frame.grid(row=1, column=0)


output_frame = tk.Frame(
    master=main_frame, padx=10, pady=10, borderwidth=2, relief=tk.RAISED
)
output_text = tk.Text(master=output_frame, height=10)
output_text.pack()
output_frame.grid(row=2, column=0)

main_window.mainloop()
