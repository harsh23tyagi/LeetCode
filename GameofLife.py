class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
#       Give 4 to a cell turned from live to dead
#       Give 3 to a cell turned from dead to live
#       Give 0 to a cell if dead remains dead
#       Give 1 to a cell if live remains dead

        m = len(board)
        if(m == 0):
            return
        m -= 1
        n = len(board[0])
        if(n == 0):
            # here we will right logic for a single columned or single rowed matrix
            return
        n -= 1
        a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
        finalList = []
        aol = Solution()
        print(board)
        for i in range(m+1):
            tempList = []
            for j in range(n+1):
                a = int(aol.elementCheck(
                    aol.checkBorder(i-1, j-1, m, n, board)))
                b = int(aol.elementCheck(aol.checkBorder(i-1, j, m, n, board)))
                c = int(aol.elementCheck(
                    aol.checkBorder(i-1, j+1, m, n, board)))
                d = int(aol.elementCheck(aol.checkBorder(i, j-1, m, n, board)))
                e = int(aol.elementCheck(aol.checkBorder(i, j+1, m, n, board)))

                f = int(aol.elementCheck(
                    aol.checkBorder(i+1, j-1, m, n, board)))
                g = int(aol.elementCheck(aol.checkBorder(i+1, j, m, n, board)))
                h = int(aol.elementCheck(
                    aol.checkBorder(i+1, j+1, m, n, board)))
                sumList = a+b+c+d+e+f+g+h
                if(sumList == 3):
                    if(board[i][j] == 0):
                        board[i][j] = 3
                    if(board[i][j] == 4):
                        board[i][j] = 1
                if(sumList < 2 or sumList > 3):
                    if(board[i][j] == 3):
                        board[i][j] == 0
                    elif(board[i][j] == 1):
                        board[i][j] = 4

                tempList.append(sumList)
            finalList.append(tempList)
        print(finalList)

        for i in range(m+1):
            for j in range(n+1):
                if(board[i][j] == 3):
                    board[i][j] = 1
                elif(board[i][j] == 4):
                    board[i][j] = 0
        print(board)

    def elementCheck(self, elem):
        if(elem == 4):
            return 1
        if(elem == 3):
            return 0
        if(elem == 1):
            return 1
        if(elem == 0):
            return 0

    def checkBorder(self, i, j, m, n, matrix):
        if(i < 0 or j < 0):
            return 0
        elif(i > m or j > n):
            return 0
        else:
            return matrix[i][j]


def main():
    # matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    matrix = [[0], [1], [1], [0], [1]]
    sol = Solution()
    sol.gameOfLife(matrix)


if __name__ == "__main__":
    main()
    pass
