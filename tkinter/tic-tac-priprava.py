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

    def set_text(self, text):
        self.config(text=text)

    def clear(self):
        self.config(text="")


class TopBar(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(
            text=f"Turn: {turn}",
            relief=tk.RAISED,
            borderwidth=2,
            padx=10,
            pady=10,
            *args,
            **kwargs,
        )

    def write_in_warning(self, text):
        self.config(bg="red", text=text)

    def write_normal(self, text):
        self.config(bg=default_color, text=text)


top_bar_label = TopBar(master=window)
top_bar_label.pack(pady=10, padx=5, fill="x", expand=True)


button_frame = tk.Frame(
    master=window,
)
button_frame.pack()


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
    pressed_button: TicTacButton = event.widget
    if game_plan[pressed_button.get_row()][pressed_button.get_col()] == 0:
        game_plan[pressed_button.get_row()][pressed_button.get_col()] = turn
        pressed_button.set_text(turn)
        winner = check_winner()
        if winner != 0:
            top_bar_label.write_normal(f"Winner is {winner}")
            print(f"Winner is {winner}")
            [button.clear() for button in all_buttons]

            turn = "O"
            return
        turn = "X" if turn == "O" else "O"
        top_bar_label.write_normal(f"Turn: {turn}")
    else:
        top_bar_label.write_in_warning("Illegal move")
        print("Illegal move")
    print(game_plan)


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


def reset_game(event):
    turn = "O"
    top_bar_label.write_normal(f"Turn {turn}")
    [button.clear() for button in all_buttons]


reset_button = tk.Button(master=window, relief=tk.RAISED, text="Reset")
reset_button.pack(padx=5, pady=5, fill="x", expand=True)
reset_button.bind("<Button>", reset_game)

window.mainloop()
