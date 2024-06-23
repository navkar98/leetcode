from functools import cache

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # n = len(nums)

        # @cache
        # def solve(idx, max_value, min_value, length):
        #     if idx >= n:
        #         return length
            
        #     with_previous = length
        #     max_value = max(max_value, nums[idx])
        #     min_value = min(min_value, nums[idx])
            
        #     if max_value - min_value <= limit:
        #         with_previous = solve(idx + 1, max_value, min_value, length + 1)
            
        #     without_previous = solve(idx + 1, nums[idx], nums[idx], 1)

        #     return max(with_previous, without_previous)

        # return solve(0, nums[0], nums[0], 0)

        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length