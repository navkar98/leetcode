from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_listed = []
        listed = defaultdict(int)
        arr2_set = set(arr2)
        ans = []

        for i in arr1:
            if i in arr2_set:
                listed[i] += 1
            else:
                not_listed.append(i)
        
        for i in arr2:
            ans.extend([i]*listed[i])

        return ans + sorted(not_listed)