class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = [(grid[0][0], 0, 0)]
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        while queue:
            # print(queue)
            depth, i, j = heapq.heappop(queue)

            ans = max(ans, depth)
            visited.add((i,j))
            
            if i == m-1 and j == n-1:
                return ans

            if i - 1 >= 0 and (i-1, j) not in visited:
                heapq.heappush(queue, (grid[i-1][j], i-1, j))
            if j - 1 >= 0 and (i, j-1) not in visited:
                heapq.heappush(queue, (grid[i][j-1], i, j-1))
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(queue, (grid[i + 1][j], i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(queue, (grid[i][j + 1], i, j + 1))
            
        return ans