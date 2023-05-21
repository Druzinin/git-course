class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols] * rows

    def __str__(self):
        output = ''
        for i in range(self.rows):
            row = ''
            for j in range(self.cols):
                row += str(self.grid[i][j]) + '\t'
            output += row + '\n'
        return output

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.grid[i][j] = self.grid[i][j] + other.grid[i][j]
            return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.grid[i][j] = self.grid[i][j] - other.grid[i][j]
            return result

    def __mul__(self, other):
        if self.cols != other.rows:
            return None
        else:
            result = Matrix(self.rows, other.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    total = 0
                    for k in range(self.cols):
                        total += self.grid[i][k] * other.grid[k][j]
                    result.grid[i][j] = total
            return result


# создание матриц
a = Matrix(2, 2)
a.grid = [[1, 2], [3, 4]]
print('Матрица a')
print(a)

b = Matrix(2, 2)
b.grid = [[5, 6], [7, 8]]
print('Матрица b')
print(b)

# сложение матриц
c = a + b
print('сложение матриц')
print(c)

# вычитание матриц
d = a - b
print('вычитание матриц')
print(d)

# умножение матриц
e = a * b
print('умножение матриц')
print(e)
