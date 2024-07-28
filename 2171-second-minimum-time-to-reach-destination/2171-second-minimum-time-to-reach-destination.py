class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)        

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0

        while q:
            x, freq = q.popleft()
            t = dist1[x] if freq == 1 else dist2[x]

            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time

            for i in adj[x]:
                if dist1[i] == -1:
                    dist1[i] = t
                    q.append((i, 1))
                elif dist2[i] == -1 and dist1[i] != t:
                    if i == n:
                        return t

                    dist2[i] = t
                    q.append((i, 2))

        return 0