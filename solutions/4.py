from collections import namedtuple

with open('inputs/4') as f:
    # l = [int(x) for x in f]
    l = f.read().split('\n\n')

# Part 1

Pos = namedtuple('Pos', ['row', 'col'])

class Field(int):
    def __init__(self, *_):
        self.called = False
        
    def __repr__(self):
        return f'{super().__repr__()}-{self.called}'

class Board:
    def __init__(self, b):
        self.board: list[list[Field]] = [[Field(y) for y in x.split(' ')] for x in [a.removeprefix(' ').replace('  ', ' ') for a in b.split('\n')]]
        self.winning_number = None

    def get_pos(self, n):
        has_number = False
        for row_nr, row in enumerate(self.board):
            if n in row:
                col_nr = row.index(n)
                has_number = True
                break
        return Pos(row_nr, col_nr) if has_number else None
        
    def mark(self, n):
        pos = self.get_pos(n)
        if pos:
            self.board[pos.row][pos.col] = None
        if self.is_winning():
            self.winning_number = n
            return True
        return False
    
    def is_winning(self):
        winning_row = any(all(num is None for num in row) for row in self.board)
        winning_column = any(all(num is None for num in column) for column in zip(*self.board))
        return winning_row or winning_column
    
    def print_score(self):
        sum_ = sum(sum(num for num in row if num is not None) for row in self.board)
        print(sum_ * self.winning_number)

    def check_win(self):
        return self.winning_number is not None

    def __repr__(self):
        return repr(self.board)

numbers = [int(x) for x in l[0].split(',')]
boards = [Board(b) for b in l[1:]]

def part1():
    for n in numbers:
        for board in boards:
            if board.mark(n):
                return board.print_score()

part1()

# Part 2

def part2():
    for n in numbers:
        for board in boards:
            if not board.check_win():
                if board.mark(n):
                    if sum(1 for board in boards if not board.check_win()) == 0:
                        return board.print_score()

part2()