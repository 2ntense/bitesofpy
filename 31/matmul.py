class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        return Matrix(
            [[sum(x * other.values[i][col] for i, x in enumerate(row)) for col in range(len(other.values[0]))] for
             row in self.values])

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        return self.__matmul__(other)
