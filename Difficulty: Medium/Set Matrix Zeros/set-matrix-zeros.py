class Solution:
    def setMatrixZeroes(self, mat):
        r = len(mat)
        c = len(mat[0])

        rowtrack = [0 for _ in range(r)]
        coltrack = [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(r):
            for j in range(c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    mat[i][j] = 0