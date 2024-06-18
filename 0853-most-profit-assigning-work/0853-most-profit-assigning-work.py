class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_and_profit = sorted(list(zip(difficulty, profit)))
        curr_max_profit = 0
        profit_at_diff = {}
        idx = 0
        n = len(diff_and_profit)

        for i in range(100000):
            while idx < n and i == diff_and_profit[idx][0]:
                curr_max_profit = max(curr_max_profit, diff_and_profit[idx][1])
                idx += 1

            profit_at_diff[i] = curr_max_profit

        ans = 0

        for i in worker:
            ans += profit_at_diff[i]

        return ans

