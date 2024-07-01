class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        curr_sum = 0

        for i in arr:
            curr_sum += i
            
            if i %2 == 0:
                curr_sum = 0
            elif curr_sum != i and curr_sum %2 != 0:
                return True

        return False
            