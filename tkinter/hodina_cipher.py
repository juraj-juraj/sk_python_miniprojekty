import tkinter as tk

main_window = tk.Tk()
main_window.title("Cipher program")

main_frame = tk.Frame(master=main_window, height=400, width=400)
main_frame.pack()

control_frame = tk.Frame(master=main_frame)
control_frame.grid(row=0, column=0)
input_label = tk.Label(master=control_frame, text="Zadaj text")
input_label.grid(row=0, column=0)
cipher_button = tk.Button(master=control_frame, text="Zasifruj")
cipher_button.grid(row=0, column=1)

input_frame = tk.Frame(
    master=main_frame, padx=10, pady=10, borderwidth=2, relief=tk.RAISED
)
input_frame.grid(row=1, column=0)
input_text = tk.Text(master=input_frame, height=10)
input_text.pack()

output_frame = tk.Frame(
    master=main_frame, padx=10, pady=10, borderwidth=2, relief=tk.RAISED
)
output_frame.grid(row=2, column=0)
output_text = tk.Text(master=output_frame, height=10)
output_text.pack()

main_window.mainloop()
