class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges, n):
            adj = [[] for _ in range(n + 1)]
            deg = [0] * (n + 1)
            order = []
            for x in edges:
                adj[x[0]].append(x[1])
                deg[x[1]] += 1
            q = deque()
            for i in range(1, n + 1):
                if deg[i] == 0:
                    q.append(i)
            while q:
                f = q.popleft()
                order.append(f)
                n -= 1
                for v in adj[f]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
            if n != 0:
                return []
            return order

        order_rows = topo_sort(rowConditions, k)
        order_col = topo_sort(colConditions, k)
        if not order_rows or not order_col:
            return []

        ans = [[0] * k for _ in range(k)]
        pos = {}
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_col[j]:
                    ans[i][j] = order_rows[i]

        return ans

            

        
                 