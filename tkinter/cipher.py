import tkinter

window = tkinter.Tk()
window.title("Cipher")

main_frame = tkinter.Frame(window, height=400, width=400)
main_frame.pack()

input_field = tkinter.Frame(main_frame)
input_field.grid(row=0, column=0)

input_label = tkinter.Label(input_field, text="zadaj text:")
input_label.grid(row=0, column=0)
input_entry = tkinter.Entry(input_field)
input_entry.grid(row=0, column=1)
ipnut_button = tkinter.Button(input_field, text="Zašifruj")
ipnut_button.grid(row=0, column=2)

output_field = tkinter.Frame(
    main_frame, padx=10, pady=10, height=200, relief=tkinter.RAISED, borderwidth=2
)
output_field.grid(row=1, column=0)

output_text = tkinter.Text(output_field, height=20)
output_text.delete(1.0, tkinter.END)
output_text.insert(tkinter.END, "ahoj")
output_text.pack()

window.mainloop()
