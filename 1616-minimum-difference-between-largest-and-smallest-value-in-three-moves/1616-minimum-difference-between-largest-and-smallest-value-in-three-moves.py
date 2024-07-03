class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n > 4:
            return min(nums[n-1-3] - nums[0], nums[n-1] - nums[3], nums[n-1-2] - nums[1], nums[n-2] - nums[2])
        else:
            return 0