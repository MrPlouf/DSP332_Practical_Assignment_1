class GameLogic:
    @staticmethod
    def valid_moves(number):
        return [move for move in (2, 3) if number % move == 0]

    @staticmethod
    def apply_move(number, move, player):
        if move == 2:
            number //= 2
            score = 2
        elif move == 3:
            number //= 3
            score = 3
        else:
            raise ValueError("Invalid move")

        return number, score if player == 'human' else -score

    @staticmethod
    def is_game_over(number):
        return number <= 10 or not GameLogic.valid_moves(number)

