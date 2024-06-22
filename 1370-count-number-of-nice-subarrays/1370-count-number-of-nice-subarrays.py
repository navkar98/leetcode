class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        curr_sum = 0
        ans = 0
        
        for i in nums:
            curr_sum += i
            if curr_sum >= k:
                ans += prefix[curr_sum - k]
            prefix[curr_sum] += 1
        
        return ans