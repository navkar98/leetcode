class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        n = len(position)
        low = 1
        high = position[-1] - position[0]
        ans = 0

        def isPossible(val):
            balls = 1
            last = position[0]
            for i in range(1, n):
                if position[i] - last >= val:
                    last = position[i]
                    balls += 1
            # print(val, balls)
            return balls >= m

        while low <= high:
            mid = (low + high)//2
            # mid_2 = low + (high - low) // 2
            # print(mid, mid_2)

            if isPossible(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1

        return ans
