import pygame
import math
import random
from constants import *


class Cell:
    def __init__(self):
        self.revealed = 0
        self.bomb = 0
        self.adjacentBombs = 0

    def revealCell(self):
        self.revealed = 1

    def placeBomb(self):
        self.bomb = 1

    def placeAdjacentBombs(self, bombs: int):
        self.adjacentBombs = bombs


class Minesweeper:
    def __init__(self, _dimensions: (int, int)):
        self.dimensions = _dimensions
        self.cellGrid = self.initCellGrid()
        self.moves = 0

    def initCellGrid(self):
        temp = []
        for row in range(self.dimensions[0]):
            temp.append([])
            for col in range(self.dimensions[1]):
                temp[row].append(Cell())
        return temp

    def validPos(self, row, col):
        return not (row < 0 or col < 0 or row > self.dimensions[0] - 1 or col > self.dimensions[1] - 1)

    def generateAdjacentBombs(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                count = 0
                if self.validPos(i-1, j-1):
                    if self.cellGrid[i-1][j-1].bomb:
                        count += 1
                if self.validPos(i, j-1):
                    if self.cellGrid[i][j-1].bomb:
                        count += 1
                if self.validPos(i+1, j-1):
                    if self.cellGrid[i + 1][j - 1].bomb:
                        count += 1
                if self.validPos(i-1, j):
                    if self.cellGrid[i - 1][j].bomb:
                        count += 1
                if self.validPos(i+1, j):
                    if self.cellGrid[i + 1][j].bomb:
                        count += 1
                if self.validPos(i-1, j+1):
                    if self.cellGrid[i - 1][j + 1].bomb:
                        count += 1
                if self.validPos(i, j+1):
                    if self.cellGrid[i][j + 1].bomb:
                        count += 1
                if self.validPos(i+1, j+1):
                    if self.cellGrid[i + 1][j + 1].bomb:
                        count += 1
                self.cellGrid[i][j].adjacentBombs = count

    def generateBombs(self, pos: (int, int)):
        x = self.dimensions[0] * self.dimensions[1]

        bombsToGenerate = math.ceil(0.0002 * x ** 2 + 0.1044 * x + 0.2979)  # Equation to generate bombs

        while bombsToGenerate > 0:
            i = random.randint(0, self.dimensions[0] - 1)
            j = random.randint(0, self.dimensions[1] - 1)
            if self.cellGrid[i][j].bomb == 0 and (i, j) != pos:
                self.cellGrid[i][j].bomb = 1
                bombsToGenerate -= 1

        self.generateAdjacentBombs()
        it

    def incrMoves(self):
        self.moves += 1


def mouseHandler(game: Minesweeper):  # Register the locations of each of the boxes
    mouse = pygame.mouse.get_pos()
    X = 0
    Y = 200
    for i in range(game.dimensions[0]):
        for j in range(game.dimensions[1]):
            if X <= mouse[0] < X + (GRID_WIDTH / game.dimensions[1]) and Y <= mouse[1] < Y + (GRID_HEIGHT / game.dimensions[0]):
                game.cellGrid[i][j].revealed = 1
                game.incrMoves()
                return [i, j]
            X += GRID_WIDTH / game.dimensions[1]
        Y += GRID_HEIGHT / game.dimensions[0]
        X = 0

