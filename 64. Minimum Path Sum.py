class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # min_sum = [[0 for _ in range(n)] for _ in range(m)]
        @cache
        def get_min_sum(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return 1e9
            min_sum = min(get_min_sum(i-1, j), get_min_sum(i, j-1)) + grid[i][j]
            # print(i, j, grid[i][j], min_sum)
            return min_sum
        return get_min_sum(m-1, n-1)