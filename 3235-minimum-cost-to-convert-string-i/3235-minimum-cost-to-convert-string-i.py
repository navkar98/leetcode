class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = collections.defaultdict(dict)

        for f, t, c in zip(original, changed, cost):
            if f in adj and t in adj[f] and adj[f][t] > c:
                adj[f][t] = c
            elif f not in adj or (f in adj and t not in adj[f]):
                adj[f][t] = c

        paths = {}
        def explore_min_paths(node):
            curr_paths = {node: 0}

            heap = [(0, node)]

            while heap:
                curr_cost, curr_node = heapq.heappop(heap)

                for t in adj[curr_node]:
                    if t not in curr_paths or (t in curr_paths and curr_paths[t] > curr_cost + adj[curr_node][t]):
                        curr_paths[t] = curr_cost + adj[curr_node][t]
                        heapq.heappush(heap, (curr_cost + adj[curr_node][t], t))
            
            return curr_paths

        for i in set(original):
            paths[i] = explore_min_paths(i)

        ans = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if source[i] not in paths or (source[i] in paths and target[i] not in paths[source[i]]):
                    return -1

                ans += paths[source[i]][target[i]]

        return ans