import tkinter as tk

window = tk.Tk()

window.title("Tic Tac Toe")

game_plan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


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

turn = "O"


def check_winner():
    for row in range(3):
        if game_plan[row][0] == game_plan[row][1] == game_plan[row][2]:
            return game_plan[row][0]

    for collumn in range(3):
        if game_plan[0][collumn] == game_plan[1][collumn] == game_plan[2][collumn]:
            return game_plan[0][collumn]

    if game_plan[0][0] == game_plan[1][1] == game_plan[2][2]:
        return game_plan[0][0]
    if game_plan[0][2] == game_plan[1][1] == game_plan[2][0]:
        return game_plan[0][2]

    return 0


def press_button(event):
    global turn
    global game_plan
    pressed_button = event.widget
    if game_plan[pressed_button.get_row()][pressed_button.get_col()] == 0:
        game_plan[pressed_button.get_row()][pressed_button.get_col()] = turn
        pressed_button.config(text=turn)
        winner = check_winner()
        if winner != 0:
            print(f"Winner is {winner}")
        turn = "X" if turn == "O" else "O"
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
            "<Button>", press_button
        )  # Pripojíme funkciu, ktorá sa spustí pri ľavom kliknutí. <Button-1> znamená ľavé tlačítko.

window.mainloop()
