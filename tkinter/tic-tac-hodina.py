import tkinter as tk

window = tk.Tk()

window.title("Tic Tac Toe")

game_plan = [[0] * 3 for _ in range(3)]


class TicTacButton(
    tk.Button
):  # Vytvoríme si novú triedu, ktorá bude dediť od tk.Button.
    def set_position(
        self, col, row
    ):  # Metóda, ktorá nastaví pozíciu tlačítka a zapamätá si ju v self.
        self.col = col
        self.row = row

    def get_col(self):  # Metóda, ktorá vráti stĺpec tlačítka, v ktorom sa nachádza.
        return self.col

    def get_row(self):  # Metóda, ktorá vráti riadok tlačítka, v ktorom sa nachádza.
        return self.row


button_frame = tk.Frame(master=window)
button_frame.pack()


def press_right_button(
    event,
):  # Funkcia, ktorá sa spustí pri pravom kliknutí na tlačítko.
    pressed_button: TicTacButton = (
        event.widget
    )  # Zistíme, ktoré tlačítko bolo stlačené.
    if (
        game_plan[pressed_button.get_row()][pressed_button.get_col()] == 0
    ):  # Ak je políčko prázdne, zapíšeme tam X.
        game_plan[pressed_button.get_row()][pressed_button.get_col()] = "X"
        pressed_button.config(text="X")  # Zmeníme text tlačítka na X.
    else:
        print("Illegal move")  # Ak políčko nie je prázdne, vypíšeme chybovú hlášku.
    print(game_plan)


def press_left_button(event):
    pressed_button: TicTacButton = event.widget
    if game_plan[pressed_button.get_row()][pressed_button.get_col()] == 0:
        game_plan[pressed_button.get_row()][pressed_button.get_col()] = "O"
        pressed_button.config(text="O")
    else:
        print("Illegal move")
    print(game_plan)


for act_row in range(3):
    for act_col in range(3):
        temp_button = TicTacButton(
            master=button_frame, height=3, width=5
        )  # Vytvoríme button, tentoraz ale už ako nami definované TicTacButton.
        temp_button.grid(row=act_row, column=act_col, padx=3, pady=3)
        temp_button.set_position(
            col=act_col, row=act_row
        )  # Nastavíme pozíciu tlačítka.
        temp_button.bind(
            "<Button-1>", press_left_button
        )  # Pripojíme funkciu, ktorá sa spustí pri ľavom kliknutí. <Button-1> znamená ľavé tlačítko.
        temp_button.bind(
            "<Button-3>", press_right_button
        )  # Pripojíme funkciu, ktorá sa spustí pri pravom kliknutí. <Button-3> znamená pravé tlačítko.

window.mainloop()


