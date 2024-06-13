import tkinter as tk

turn = "O"
window = tk.Tk()

window.title("Tic Tac Toe")
default_color = window.cget("bg")

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

    def clear(self):
        self.config(text="")


class TopBarLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(
            text=f"Turn: {turn}",
            pady=10,
            relief=tk.RAISED,
            borderwidth=3,
            *args,
            **kwargs,
        )

    def write_warning(self, warning_text):
        self.config(text=warning_text, bg="red")

    def write_normal(self, text):
        self.config(text=text, bg=default_color)


top_bar_label = TopBarLabel(master=window)
top_bar_label.pack(pady=10, padx=5, fill="x")

button_frame = tk.Frame(master=window)
button_frame.pack()


def check_winner():
    for row in range(3):
        if game_plan[row][0] != 0 and (
            game_plan[row][0] == game_plan[row][1] == game_plan[row][2]
        ):
            return game_plan[row][0]

    for collumn in range(3):
        if game_plan[0][collumn] != 0 and (
            game_plan[0][collumn] == game_plan[1][collumn] == game_plan[2][collumn]
        ):
            return game_plan[0][collumn]

    if game_plan[0][0] != 0 and (game_plan[0][0] == game_plan[1][1] == game_plan[2][2]):
        return game_plan[0][0]
    if game_plan[0][2] != 0 and (game_plan[0][2] == game_plan[1][1] == game_plan[2][0]):
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
            top_bar_label.write_normal(f"Winner is {winner}")
            reset_game(overwrite_top_label=False)
            return
        turn = "X" if turn == "O" else "O"
        top_bar_label.write_normal(f"Turn: {turn}")
    else:
        top_bar_label.write_warning("Illegal move")
        print("Illegal move")
    print(game_plan)


def reset_game(*args, overwrite_top_label=True):
    global game_plan
    global turn
    for button in all_buttons:
        button.clear()
    game_plan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    turn = "O"
    if overwrite_top_label:
        top_bar_label.write_normal(f"Turn: {turn}")


all_buttons = []
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
        all_buttons.append(temp_button)

reset_button = tk.Button(master=window, text="Reset", relief=tk.RAISED, pady=5)
reset_button.pack(pady=5, padx=5, fill="x")
reset_button.bind("<Button>", reset_game)

window.mainloop()
