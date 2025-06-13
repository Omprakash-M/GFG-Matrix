class Solution:
    def rotateMatrix(self, k, mat):
        for i in range(len(mat)):
            k_mod = k % len(mat[i])  # handle k > len(row)
            mat[i] = mat[i][k_mod:] + mat[i][:k_mod]
        return mat
