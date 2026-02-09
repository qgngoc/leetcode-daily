class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        j = 0
        direction = "r"
        value = 1
        max_left = 0
        max_right = n - 1
        max_up = 1
        max_down = n - 1
        while value <= n*n:
            # print(i, j, value)
            matrix[i][j] = value
            value += 1
            if direction == 'r':
                if j == max_right:
                    direction = 'd'
                    max_right -= 1
                    i += 1
                else:
                    j += 1
            elif direction == 'd':
                if i == max_down:
                    direction = 'l'
                    max_down -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == 'l':
                if j == max_left:
                    direction = 'u'
                    max_left += 1
                    i -= 1
                else:
                    j -= 1
            elif direction == 'u':
                if i == max_up:
                    direction = 'r'
                    max_up += 1
                    j += 1
                else:
                    i -= 1
        return matrix