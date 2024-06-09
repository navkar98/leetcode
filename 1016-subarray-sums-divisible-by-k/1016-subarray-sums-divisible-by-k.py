from functools import cache

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum = 0
        d = {0:1}

        for num in nums:
            prefix_sum+=num
            
            if prefix_sum%k in d:
                ans+=d[prefix_sum%k]
                d[prefix_sum%k]+=1
            else:
                d[prefix_sum%k] = 1
        
        return ans