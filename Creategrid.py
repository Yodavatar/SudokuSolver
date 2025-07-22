#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver

import random

class Cell:
    """This class represent a cell of Sudoku game"""
    def __init__(self,i,j,value):
        self.value = value
        self.possibility = [1,2,3,4,5,6,7,8,9]
        self.i = i
        self.j = j
    
    def get_value(self) -> int: return self.value

    def defined(self) -> bool:
        """return a bool is the cell is define or not"""
        if self.value == 0:
            return False
        return True

class Grid:
    """This class represent the grid of the sudoku"""
    def __init__(self) -> None:
        self.grid = []

    def create_grid(self) -> None:
        """function for create a grid of 0 anywhere"""
        self.grid = []
        for i in range(9):
            self.grid.append([])
            for j in range(9):
                self.grid[i].append(Cell(i,j,0))
    
    def get_grid(self,grid :list) -> None:
        """remplace self.grid by a list of list"""
        for i in range(9):
            for j in range(9):
                self.grid[i][j].value = grid[i][j]
    
    def create_sudoku_grid(self)-> None:
        """This fonction create a grid of sudoku"""
        all_defined = False
        while all_defined == False:
            really_all_defined = True
            for line in self.grid:
                for cell in line:
                    if cell.defined:
                        print("defined")
                    else:
                        print("ok")
                        really_all_defined = False
                        cell.value = random.choices(cell.possibility)
                        rect = self.get_rect(cell)
                        rect.remove(cell)
                        line = self.get_line(cell)
                        line.remove(cell)
                        collumn = self.get_collumn(cell)
                        collumn.remove(cell)
                        
                        for rect_cell in rect:
                                if rect_cell.defined():
                                    pass
                                else:
                                    #check the possibility for the cell
                                    possibility_line = self.get_line_value(rect_cell)
                                    possibility_collumn = self.get_collumn_value(rect_cell)
                                    possibility_rect = self.get_rect_value(rect_cell)

                                    remove_possibility = []
                                    for cell_possibility in rect_cell.possibility:
                                        if cell_possibility in possibility_line:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_collumn:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_rect:
                                            remove_possibility.append(cell_possibility)
                                    for rm in remove_possibility:
                                        rect_cell.possibility.remove(rm)

                        for line_cell in line:
                                if line_cell.defined():
                                    pass
                                else:
                                    #check the possibility for the cell
                                    possibility_line = self.get_line_value(line_cell)
                                    possibility_collumn = self.get_collumn_value(line_cell)
                                    possibility_rect = self.get_rect_value(line_cell)

                                    remove_possibility = []
                                    for cell_possibility in line_cell.possibility:
                                        if cell_possibility in possibility_line:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_collumn:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_rect:
                                            remove_possibility.append(cell_possibility)
                                    for rm in remove_possibility:
                                        line_cell.possibility.remove(rm)

                        for collumn_cell in collumn:
                                if collumn_cell.defined():
                                    pass
                                else:
                                    #check the possibility for the cell
                                    possibility_line = self.get_line_value(collumn_cell)
                                    possibility_collumn = self.get_collumn_value(collumn_cell)
                                    possibility_rect = self.get_rect_value(collumn_cell)

                                    remove_possibility = []
                                    for cell_possibility in collumn_cell.possibility:
                                        if cell_possibility in possibility_line:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_collumn:
                                            remove_possibility.append(cell_possibility)
                                        elif cell_possibility in possibility_rect:
                                            remove_possibility.append(cell_possibility)
                                    for rm in remove_possibility:
                                        collumn_cell.possibility.remove(rm)
            if really_all_defined:
                all_defined = True
                 
    def get_line_value(self,cell:Cell) -> list:
        """return the line where is the cell"""
        line = []
        for cell in self.grid[cell.i]:
            line.append(cell.get_value())
        return line
    
    def get_line(self,cell:Cell) -> list:
        """return the line of cells where is the cell"""
        line = []
        for cell in self.grid[cell.i]:
            line.append(cell)
        return line

    def get_collumn_value(self,cell:Cell) -> list:
        """return the collumn where is the cell"""
        collumn = []
        for line in self.grid:
            collumn.append(line[cell.j].get_value())
        return collumn
   
    def get_collumn(self,cell:Cell) -> list:
        """return the collumn where is the cell"""
        collumn = []
        for line in self.grid:
            collumn.append(line[cell.j])
        return collumn

    def get_rect_value(self,cell:Cell) -> list:
        """return the rect where is the cell"""
        rect = []
        coord_i,coord_j = int(cell.i/3),int(cell.j/3)
        start_i,start_j = coord_i*3,coord_j*3
        for indice_line in range(0,9):
            if indice_line >= start_i and indice_line <= start_i+2:
                for indice_cell in range(0,9):
                    if indice_cell >= start_j and indice_cell <= start_j+2:
                        rect.append(self.grid[indice_line][indice_cell].get_value())
                    else:
                        pass
            else:
                pass
        return rect

    def get_rect(self,cell:Cell) -> list:
        """return the rect where is the cell"""
        rect = []
        coord_i,coord_j = int(cell.i/3),int(cell.j/3)
        start_i,start_j = coord_i*3,coord_j*3
        for indice_line in range(0,9):
            if indice_line >= start_i and indice_line <= start_i+2:
                for indice_cell in range(0,9):
                    if indice_cell >= start_j and indice_cell <= start_j+2:
                        rect.append(self.grid[indice_line][indice_cell])
                    else:
                        pass
            else:
                pass
        return rect

    def __str__(self) -> str:
        result = ""
        for line in self.grid:
            for cell in line:
                result += str(cell.value)+","
            result+="\n"
        return result[0:-1]


if __name__ == "__main__":
    grid = Grid()
    grid.create_grid()
    grid.create_sudoku_grid()
    print(grid)



#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver