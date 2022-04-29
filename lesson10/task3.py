class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells+other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError("У первой клеток меньше, чем у второй")

    def __mul__(self, other):
        return Cell(self.cells*other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells//other.cells)

    # новая клетка должна принимать целое число, поэтому по сути реализация __truediv__ сводится к __floordiv__
    def __truediv__(self, other):
        return Cell(self.cells//other.cells)

    def make_order(self, count_cells_row):
        count_rows = self.cells // count_cells_row
        line = ""
        for i in range(count_rows):
            for j in range(count_cells_row):
                line += "*"
            line += "\n"
        for i in range(self.cells - count_rows*count_cells_row):
            line += "*"
        return line


if __name__ == "__main__":
    c1 = Cell(100)
    c2 = Cell(6)
    c3 = c1/c2
    c4 = c1-c2
    c5 = c1*c2
    print(c3.cells, c4.cells, c5.cells, sep="  ")
    print(c1.make_order(9))
