from collections import defaultdict

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        curr_flip = 0
        ans = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if i >= k and nums[i-k]==2:
                curr_flip -= 1
            
            if curr_flip%2 == num:
                if i + k > len(nums):
                    return -1

                curr_flip += 1
                ans += 1
                nums[i] = 2
            
        return ans