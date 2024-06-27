class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = nums[0]
        max_reach_last_index = 0
        n = len(nums)
        ans = 1
        i = 0

        if nums[0] <= 0 and n > 1:
            return 0
        if nums[0] >= 0 and n == 1:
            return 0

        while i < n:
            if max_reach >= n- 1:
                return ans
            
            new_reach = max(i + nums[i], max_reach)

            while i <= new_reach:
                curr_reach = i + nums[i]
                if curr_reach > max_reach:
                    max_reach = curr_reach
                
                i+= 1

            # print(max_reach)
            i = new_reach
            ans += 1

        return ans