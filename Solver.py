#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver

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
    
    def resolution(self) -> None:
        """found the solution of the sudoku not finished"""
        old_grid = ""
        while old_grid != self.__str__():
            old_grid = self.__str__()
            self.found_value()

    def found_value(self) -> None:
        """Sort the possibility of each cell of the sudoku grid"""
        for line in self.grid:
            for cell in line:
                if cell.defined():
                    pass
                else:
                    possibility_line = self.get_line_value(cell)
                    possibility_collumn = self.get_collumn_value(cell)
                    possibility_rect = self.get_rect_value(cell)

                    #check the possibility for the cell
                    remove_possibility = []
                    for cell_possibility in cell.possibility:
                        if cell_possibility in possibility_line:
                            remove_possibility.append(cell_possibility)
                        elif cell_possibility in possibility_collumn:
                            remove_possibility.append(cell_possibility)
                        elif cell_possibility in possibility_rect:
                            remove_possibility.append(cell_possibility)
                    for rm in remove_possibility:
                        cell.possibility.remove(rm)

                    #calcul the solution and possibility per cell
                    if len(cell.possibility) == 1:
                        cell.value = cell.possibility[0]
                        #print("Value found : "+str(cell.possibility[0])+" in line "+str(cell.i+1)+" ,Collumn "+str(cell.j+1))
                    else:
                        rect = self.get_rect(cell)
                        rect.remove(cell)
                        line = self.get_line(cell)
                        line.remove(cell)
                        collumn = self.get_collumn(cell)
                        collumn.remove(cell)
                        for cell_possibility in cell.possibility:
                            founding = True
                            #solution by rect
                            for rect_cell in rect:
                                if rect_cell.defined():
                                    pass
                                else:
                                    if cell_possibility in rect_cell.possibility:
                                        founding = False
                                    else:
                                        pass
                            if founding:
                                cell.value = cell_possibility
                                #print("Value found : "+str(cell.possibility[0])+" in line "+str(cell.i+1)+" ,Collumn "+str(cell.j+1))
                                break
                            #solution by line
                            for line_cell in line:
                                if line_cell.defined():
                                    pass
                                else:
                                    if cell_possibility in line_cell.possibility:
                                        founding = False
                                    else:
                                        pass
                            if founding:
                                cell.value = cell_possibility
                                #print("Value found : "+str(cell.possibility[0])+" in line "+str(cell.i+1)+" ,Collumn "+str(cell.j+1))
                                break
                            #solution by collumn
                            for collumn_cell in collumn:
                                if collumn_cell.defined():
                                    pass
                                else:
                                    if cell_possibility in collumn_cell.possibility:
                                        founding = False
                                    else:
                                        pass
                            if founding:
                                cell.value = cell_possibility
                                #print("Value found : "+str(cell.possibility[0])+" in line "+str(cell.i+1)+" ,Collumn "+str(cell.j+1))
                                break 
                 
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

def open_grid(name) -> list:
    """return a grid of a list of list of integer"""
    file_grid = []
    file = open(name,"r")
    for line in file:
        if line[-1] == "\n":
            line = line[0:-1]
        file_grid.append(line.split(","))
    file.close()
    for i in range(len(file_grid)):
        for j in range(len(file_grid[0])):
            file_grid[i][j] = int(file_grid[i][j])
    return file_grid

#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT
#App : SudokuSolver