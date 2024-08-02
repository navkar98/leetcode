class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ttl, n = sum(nums), len(nums)
        ans = float('inf')
        w_sum = sum(nums[0:ttl])
        if w_sum == ttl:
            return 0
        for idx in range(n):
            ans = min(ans, ttl - w_sum)
            w_sum -= nums[idx]
            w_sum += nums[(idx + ttl) % n]
        else:
            ans = min(ans, ttl - w_sum)
        return ans