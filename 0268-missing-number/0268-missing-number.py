class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        isZeroAvail = False
        total = 0
        n = len(nums)

        for i in nums:
            if i == 0:
                isZeroAvail = True

            total += i

        return (n*(n+1))//2 - total if isZeroAvail else 0