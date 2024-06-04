from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        q = deque()
        ans = []

        for i in range(len(nums)):
            if len(q) > 0 and q[0][0] + k - 1 < i:
                q.popleft()

            while len(q) > 0 and q[-1][1] < nums[i]:
                q.pop()

            q.append((i, nums[i]))

            if i + 1 >= k:
                ans.append(q[0][1])

        return ans