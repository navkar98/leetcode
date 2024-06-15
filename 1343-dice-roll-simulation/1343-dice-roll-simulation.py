from functools import cache

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        @cache
        def solve(idx, last, count):
            if rollMax[last] < count:
                return 0

            if idx == n:
                return 1

            ans = 0

            for i in range(6):
                ans = (ans + solve(idx + 1, i, count + 1 if i == last else 1)) % MOD

            return ans % MOD

        ans = 0

        for i in range(6):
            ans = (ans + solve(1, i, 1)) % MOD

        return ans

            