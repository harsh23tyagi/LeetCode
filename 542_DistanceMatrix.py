# Calculate te minimum distance of an element in the matrix to the nearest zero, in a matrix of 0s and 1s


class Solution:
    # def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]: leetcode definition
    def updateMatrix(self, matrix):
        lengthRows = len(matrix)
        lengthCols = len(matrix[0])
        for row in range(lengthRows):
            for col in range(lengthCols):
                if(matrix[row][col] != 0):
                    top = matrix[row-1][col] if row > 0 else 10000
                    left = matrix[row][col-1] if col > 0 else 10000
                    matrix[row][col] = min(top, left)+1
        for row in range(lengthRows)[::-1]:
            for col in range(lengthCols)[::-1]:
                if(matrix[row][col] != 0):
                    bottom = matrix[row +
                                    1][col] if row < lengthRows-1 else 10000
                    right = matrix[row][col+1] if col < lengthCols-1 else 10000
                    matrix[row][col] = min(
                        matrix[row][col], min(bottom, right)+1)
        return matrix
#         The above will be a top down parsing
# Now doing a bottom up parsing to change the distance if smaller


if __name__ == "__main__":
    sol = Solution()
    matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    answer = sol.updateMatrix(matrix)
    print(answer)
    pass


# In the above solution we went from top to bottom taking minimum of either the top or the left +1
# In the second pass we go from bottom to up taking the minimum of already existing value of either the bottom or the righ +1 or the old value which was there in the top down approach
# the initial values of the first and last rows are taken as infinity, which are replaced by second pass for the first pass if created and neglected in the second pass
