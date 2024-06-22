class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in nums:
            i = i == 1


        for i in range(n-2):
            if not nums[i]:
                nums[i] = not nums[i]
                nums[i+1] = not nums[i+1]
                nums[i+2] = not nums[i+2]
                ans +=1 
        # print(nums)
        if not nums[-1] or not nums[-2]: return -1
        else: return ans
        
                