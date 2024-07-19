class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        min_row = []
        max_col = []

        for i in range(m):
            curr_row_min = inf
            for j in range(n):
                curr_row_min = min(curr_row_min, matrix[i][j])

            min_row.append(curr_row_min)

        for j in range(n):
            curr_col_max = -inf
            for i in range(m):
                curr_col_max = max(curr_col_max, matrix[i][j])

            max_col.append(curr_col_max)

        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= min_row[i] and matrix[i][j] >= max_col[j]:
                    ans.append(matrix[i][j])

        return ans