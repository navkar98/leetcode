class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        available = 0
        idx = 0
        ans = 0
        numslen = len(nums)

        while available < n:
            if idx < numslen and nums[idx] <= available + 1:
                available += nums[idx]
                idx += 1
            else:
                ans += 1
                available += (available + 1)

        return ans