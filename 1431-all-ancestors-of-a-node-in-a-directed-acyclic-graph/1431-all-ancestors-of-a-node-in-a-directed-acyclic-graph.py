from functools import cache

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = collections.defaultdict(list)

        for u, v in edges:
            ancestors[v].append(u)

        visited = set()
        
        @cache
        def dfs(node):
            if node not in ancestors:
                return []

            anc = []
            for i in ancestors[node]:                
                anc.append(i)
                anc.extend(dfs(i))

            return list(sorted(set(anc)))

        ans = []
        for i in range(n):
            ans.append(dfs(i))
            visited = set()

        return ans