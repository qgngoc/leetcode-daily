class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_x, min_y, max_x, max_y = 1, 0, m-1, n-1
        # print(min_x, min_y, max_x, max_y)
        DIRECTION = ['r', 'd', 'l', 'u']
        output = []
        i = 0
        x = 0
        y = -1

        while len(output) < m*n:
            direction = DIRECTION[i%4]
            if direction == 'r':
                y += 1
                if y == max_y:
                    i += 1
                    max_y -= 1
            elif direction == 'd':
                x += 1
                if x == max_x:
                    i += 1
                    max_x -= 1
            elif direction == 'l':
                y -= 1
                if y == min_y:
                    i += 1
                    min_y += 1
            else:
                x -= 1
                if x == min_x:
                    i += 1
                    min_x += 1
            # print(min_x, min_y, max_x, max_y)
            # print(x, y)
            # print(output)
            # print(direction)
            # print('------')
            output.append(matrix[x][y])
        return output

