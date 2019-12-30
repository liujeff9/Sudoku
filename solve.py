from puzzles import easy 
import pygame
import sys

ROW_SIZE = 3
COL_SIZE = 3
SCREEN_SIZE = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# select puzzle and toggle to show steps of backtracking algorithm
PUZZLE = easy
SHOW = True


class Board():
    def __init__(self, board, screen, font, show):
        self.board = board
        self.screen = screen
        self.font = font
        self.show = show

    def valid_row(self, row, number):
        for index in self.board[row]:
            if index == number:
                return False
        return True

    def valid_col(self, col, number):
        for row in self.board:
            if row[col] == number:
                return False
        return True

    def valid_square(self, row, col, number):
        starting_row = row - (row % ROW_SIZE)
        starting_col = col - (col % COL_SIZE)
        for i in range(starting_row, starting_row + ROW_SIZE):
            for j in range(starting_col, starting_col + COL_SIZE):
                if self.board[i][j] == number:
                    return False
        return True

    def find_open_space(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def solve_puzzle(self):
        row, col = self.find_open_space()

        if row == -1 and col == -1:
            if not self.show:
                while True:
                    self.draw()
            return True

        for num in range(1, 10):
            
            valid = self.valid_row(row, num) and self.valid_col(col, num) and self.valid_square(row, col, num)
            
            if valid:
                self.board[row][col] = num
                
                if self.show:
                    self.draw()

                if self.solve_puzzle():
                    return True
                else:
                    self.board[row][col] = 0
        return False

    def print(self):
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                print(num, end='')
                if j == 2 or j == 5:
                    print('|', end='')
            print()
            if i == 2 or i == 5:
                print('-----------')

    def draw(self):

        screen = self.screen
        font = self.font

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)

        for i in range(1, 9):
            point = SCREEN_SIZE * i / 9
            thickness = 3 if i % 3 == 0 else 1
            
            pygame.draw.lines(screen, BLACK, False, [(point, 0), (point, SCREEN_SIZE)], thickness)
            pygame.draw.lines(screen, BLACK, False, [(0, point), (SCREEN_SIZE, point)], thickness)

        offset = SCREEN_SIZE / 18

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    number = font.render(str(self.board[row][col]), True, BLACK)

                    x = SCREEN_SIZE * row / 9 + offset
                    y = SCREEN_SIZE * col / 9 + offset

                    position = number.get_rect(center=(y, x))

                    screen.blit(number, position)

        pygame.display.update()


def run():
    pygame.init()
    font = pygame.font.SysFont("comicsansms", 50)
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    board = Board(PUZZLE, screen, font, SHOW)
    board.solve_puzzle()

if __name__ == '__main__': 
    run(easy)