#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver

from Solver import *

if __name__ == "__main__":
    gridcometofile = open_grid("grids/grid")
    grid = Grid()
    grid.create_grid()
    grid.get_grid(gridcometofile)
    grid.resolution()
    print(grid)

#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver