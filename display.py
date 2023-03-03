import pygame

from constants import *


def displayGrid(surface, dim, matrix):
    currentX = 0
    currentY = 200
    for i in range(dim[0]):
        for j in range(dim[1]):
            if matrix[i][j].revealed == 0:
                pygame.draw.rect(surface, LIGHT_BLUE if (i+j) % 2 == 0 else DARK_BLUE, pygame.Rect(currentX, currentY, GRID_WIDTH/dim[1], GRID_HEIGHT/dim[0]))
            if matrix[i][j].revealed == 1:
                pygame.draw.rect(surface, 'white', pygame.Rect(currentX, currentY, GRID_WIDTH/dim[1], GRID_HEIGHT/dim[0]))
            currentX += GRID_WIDTH/dim[1]
        currentY += GRID_WIDTH/dim[0]
        currentX = 0


