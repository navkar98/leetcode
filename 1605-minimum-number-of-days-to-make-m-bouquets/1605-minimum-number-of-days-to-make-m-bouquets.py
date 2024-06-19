class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m*k > n:
            return -1

        low = 0
        high = max(bloomDay)
        ans = inf
        
        def isPossible(num):
            curr_k = 0
            curr_m = 0
            for i in bloomDay:
                if i > num:
                    curr_k = 0
                    continue

                curr_k += 1

                if curr_k == k:
                    curr_k = 0
                    curr_m += 1
            
            return curr_m >= m

        while low <= high:
            mid = (low + high)//2

            if isPossible(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans if ans is not inf else -1

                    