from functools import cache

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if n <= 1:
            return False

        ### Memory exceeded
        # @cache
        # def solve(idx, sum_val):
        #     if idx >= n:
        #         return (sum_val % k) == 0

        #     not_relayed = False

        #     if not idx + 1 == n:
        #         not_relayed = solve(idx + 1, nums[idx])

        #     return ((nums[idx] + sum_val) % k) == 0 or not_relayed or solve(idx + 1, nums[idx] + sum_val)

        # return solve(1, nums[0])


        ### Time limit exceeded
        # prefix = set()
        
        # for i in range(n):
        #     new_set = set()
        #     if i != n - 1:
        #         new_set.add(nums[i])

        #     for j in prefix:
        #         if (nums[i] + j) % k  == 0:
        #             return True
        #         new_set.add(nums[i] + j)
            
        #     prefix = new_set
        
        # for j in prefix:
        #     if (j) % k  == 0:
        #         return True

        # return False

        ### Optimized
        prefix_remainder = {0:-1}
        total = 0
        
        for i in range(n):
            total += nums[i]
            remainder = total % k
            # print(remainder, i, prefix_remainder)

            if remainder in prefix_remainder :
                if abs(prefix_remainder[remainder] - i) > 1:
                    return True
            else:
                prefix_remainder[remainder] = i

        return False
