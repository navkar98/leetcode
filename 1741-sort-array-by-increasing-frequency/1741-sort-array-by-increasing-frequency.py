class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        distinct = collections.defaultdict(int)

        for i in nums:
            distinct[i] += 1

        distinct = sorted([(i, distinct[i]) for i in distinct.keys()], key= lambda i: (i[1],-i[0]))
        
        ans = []
        for i in distinct:
            for j in range(i[1]):
                ans.append(i[0])

        return ans 

        
