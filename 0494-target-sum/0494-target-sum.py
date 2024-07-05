from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(idx, curr_sum):
            if idx >= n:
                return 1 if curr_sum == target else 0

            return solve(idx + 1, curr_sum + nums[idx]) + solve(idx + 1, curr_sum - nums[idx])

        return solve(0, 0)