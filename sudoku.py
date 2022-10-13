import numpy as np


class Sudoku:
    def __init__(self, numbers_range: int = 9) -> None:
        # must be a quadratic number
        if np.sqrt(numbers_range) % 1 != 0:
            raise ValueError("numbers_range has to be a quadratic number")
        self.numbers_range = numbers_range
        self.numbers_cache = list(range(1, 1+self.numbers_range))


        self.dimensions = int(np.sqrt(numbers_range))
        print(self.dimensions, self.numbers_cache)

        # these are all collections. The order of the collections doesn't matter, because
        # the cells are already stored in an ordered grid
        self.rows = []
        self.collumns = []
        for i in range(self.dimensions ** 2):
            self.rows.append([])
            self.collumns.append([])
        # you acess the sqare in this list with [x][y] 0<=x<dimension 0<=y<dimension
        self.ordered_squares = []
        for i in range(self.dimensions):
            self.ordered_squares.append([])
            for j in range(self.dimensions):
                self.ordered_squares[i].append([])

        # here all the cells are stored
        self.cell_grid = []
        for x in range(self.dimensions * self.dimensions):
            self.cell_grid.append([])
            for y in range(self.dimensions * self.dimensions):
                new_cell = self.Cell(self.numbers_cache, self.get_collections_from(x, y))
                self.cell_grid[x].append(new_cell)

                self.rows[x].append(new_cell)
                self.collumns[y].append(new_cell)
                self.ordered_squares[int(x / self.dimensions)][int(y / self.dimensions)].append(new_cell)

        for collection in self.get_collections_from(0, 0):
            print()
            print(len(collection), collection)
        # print(self.cell_grid[0][0].collections)

    def get_collections_from(self, x: int, y: int):
        return [
            self.rows[x],
            self.collumns[y],
            self.ordered_squares[int(x/self.dimensions)][int(y /self.dimensions)]
        ]

    class Cell:
        def __init__(self, possibilities: list, collections: list) -> None:
            self.possibilities = possibilities[:]

            # row collums and square can each be represented as collections of cells (list)
            self.collections = collections



if __name__ == "__main__":
    sudoku = Sudoku(numbers_range=4)
