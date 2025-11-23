class Solution:
    def spiral_Matrix(self, matrix, result=None):
        if result is None:
            result = []
        
        if matrix:
            # right
            result.extend(matrix.pop(0))

            # down
            for row in matrix:
                if row:
                    result.append(row.pop())

            # left
            if matrix:
                result.extend(reversed(matrix.pop()))

            # up
            for i in range(len(matrix) - 1, -1, -1):
                if matrix[i]:
                    result.append(matrix[i].pop(0))
            
            return self.spiral_Matrix(matrix, result)
        else:
            return result

if __name__ == '__main__':
    # data = [[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]

    data = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]

    result = Solution()
    result = result.spiral_Matrix(data)
    print(result)