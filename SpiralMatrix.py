class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        #         total number of elements will be
        finalList = []
        if(not matrix):
            return finalList
        m, n = len(matrix)-1, len(matrix[0])-1
        total = (m+1)*(n+1)
        start_x = 0
        start_y = 0
        beg = 0
        counter = 0

        while(counter < total):
            while(start_y <= n and counter < total):
                finalList.append(matrix[start_x][start_y])
                start_y += 1
                counter += 1

            start_y -= 1
            start_x += 1

            while(start_x <= m and counter < total):
                finalList.append(matrix[start_x][start_y])
                start_x += 1
                counter += 1
            start_x -= 1
            start_y -= 1
            while(start_y >= beg and counter < total):
                finalList.append(matrix[start_x][start_y])
                start_y -= 1
                counter += 1
            start_y += 1
            start_x -= 1
            while(start_x > beg and counter < total):
                finalList.append(matrix[start_x][start_y])
                start_x -= 1
                counter += 1
            beg += 1
            start_x += 1
            start_y += 1
            m -= 1
            n -= 1

        return finalList


def main():
    sol = Solution()
    matrix = [[1, 2, 3, 4, 5], [7, 8, 9, 10, 11], [
        12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26]]
    # matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
    answer = sol.spiralOrder(matrix)
    print(answer)


if __name__ == "__main__":
    main()
    pass
