class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.symbol = ""

    def occupy(self, symbol):
        self.is_occupied = True
        self.symbol = symbol

    def __str__(self):
        return self.symbol if self.is_occupied else str(self.number)


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def print_board(self):
        print("┌───┬───┬───┐")
        for i in range(0, 9, 3):
            row = self.cells[i:i + 3]
            print("│ {} │ {} │ {} │".format(*row))
            if i < 6:
                print("├───┼───┼───┤")
        print("└───┴───┴───┘")

    def is_full(self):
        return all(cell.is_occupied for cell in self.cells)

    def is_winner(self, player):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

        for combination in winning_combinations:
            if all(self.cells[cell - 1].is_occupied and str(self.cells[cell - 1]) == player.symbol for cell in
                   combination):
                return True

        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name}, введите номер ячейки, чтобы сделать ход: "))
                if move < 1 or move > 9:
                    raise ValueError
                cell = board.cells[move - 1]
                if cell.is_occupied:
                    print("Ячейка уже занята. Сделайте другой ход.")
                else:
                    cell.occupy(self.symbol)
                    break
            except ValueError:
                print("Некорректный ввод. Введите число от 1 до 9.")


def play_game():
    board = Board()
    player1_name = input("Введите имя Игрока 1: ")
    player2_name = input("Введите имя Игрока 2: ")
    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")
    current_player = player1

    while True:
        print()
        board.print_board()
        current_player.make_move(board)

        if board.is_winner(current_player):
            print()
            board.print_board()
            print(f"{current_player.name} победил!")
            break
        elif board.is_full():
            print()
            board.print_board()
            print("Ничья!")
            break

        current_player = player2 if current_player == player1 else player1


play_game()
