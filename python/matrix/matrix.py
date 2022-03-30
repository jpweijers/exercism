class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        self.rows = self._get_rows()
        self.col_count = self._count_cols()

    def _get_rows(self):
        rows = self.matrix.split('\n')

        return [[int(n) for n in row.split()] for row in rows]

    def _count_cols(self):
        return len(self.matrix.split('\n'))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):

        return [self.row(i)[index-1] for i in range(1, self.col_count + 1)]
