class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        universal = set(range(2*10**5 + 1))
        unique = set()
        duplicate = []
        ans = 0

        for i in nums:
            if i not in unique:
                unique.add(i)
            else:
                duplicate.append(i)

        
        remainder = list(set(universal)^set(unique))
        duplicate.sort()
        remainder.sort()
        j = 0

        for i in range(len(duplicate)):
            while remainder[j] < duplicate[i]:
                j += 1
            ans += (remainder[j] - duplicate[i])
            j += 1

        return ans
        