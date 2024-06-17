class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        total_oranges = 0
        rotten_count = 0
        time = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_oranges += 1
                if grid[i][j] == 2:
                    total_oranges += 1
                    queue.append((i,j,0))
        
        while queue:
            i, j, curr_time = queue.pop(0)
            time = max(time, curr_time)
            rotten_count += 1

            if i - 1 >= 0 and grid[i-1][j] == 1:
                queue.append((i-1,j,curr_time+1))
                grid[i-1][j] = 2
            if j - 1 >= 0 and grid[i][j-1] == 1:
                queue.append((i,j-1,curr_time+1))
                grid[i][j-1] = 2
            if i + 1 < m and grid[i+1][j] == 1:
                queue.append((i+1,j,curr_time+1))
                grid[i+1][j] = 2
            if j + 1 < n and grid[i][j+1] == 1:
                queue.append((i,j+1,curr_time+1))
                grid[i][j+1] = 2

        if rotten_count == total_oranges:
            return time
        else:
            return -1
