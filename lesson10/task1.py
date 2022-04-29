class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        matrix = ""
        for line in self.list_of_lists:
            matrix += " ".join(list(map(str, line)))
            matrix += "\n"
        return matrix

    def __add__(self, other):
        matrix = [[el1 + el2 for el1, el2 in zip(line1, line2)]
                  for line1, line2 in zip(self.list_of_lists, other.list_of_lists)]
        return Matrix(matrix)


if __name__ == "__main__":
    m = Matrix([[3, 4, 5], [7, 6, 8]])
    n = Matrix([[2, 7, 4], [10, 20, 45]])
    print(m+n)
