class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0

        for i in nums:
            curr_val = i == 1
            if flips %2 != 0:
                curr_val = not curr_val
            
            if not curr_val:
                flips += 1
        
        return flips