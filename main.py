from display import *
from game import *


def main():
    rows = int(input("Please input the amount of rows in grid: "))
    cols = int(input("Please input the amount of columns in grid: "))
    minesweeper = Minesweeper((rows, cols))

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dimPos = mouseHandler(minesweeper)
                if minesweeper.moves == 1:
                    minesweeper.generateBombs(dimPos)

        displayGrid(screen, minesweeper.dimensions, minesweeper.cellGrid)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

