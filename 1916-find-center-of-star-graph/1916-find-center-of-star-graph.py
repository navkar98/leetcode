class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = collections.defaultdict(set)
        
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        n = len(adjList)

        for i in adjList.keys():
            if len(adjList[i]) == n-1:
                return i

        