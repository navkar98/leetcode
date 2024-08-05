from collections import OrderedDict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = OrderedDict()

        visited = set()

        for i in arr:
            if i in visited:
                d[i] = False
            else:
                d[i] = True
                visited.add(i)

        ptr = 0
        for i in d:
            if d[i]:
                ptr += 1
                if k == ptr:
                    return i
        
        return ""
