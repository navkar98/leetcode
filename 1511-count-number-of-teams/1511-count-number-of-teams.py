from functools import cache

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        greater = [0] * n
        less = [0] * n

        ans = 0

        for j in range(n):
            for i in range(j):
                if rating[i] < rating[j]:
                    greater[j] += 1
                    ans += greater[i]
                else:
                    less[j] += 1
                    ans += less[i]

        return ans