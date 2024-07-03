class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = inf
        queue = [(0, k)]
        adj_list = collections.defaultdict(list)

        for u,v,w in times:
            adj_list[u].append((v, w)) 

        visited = set()

        while queue:
            curr_time, node = heapq.heappop(queue)

            if node in visited:
                continue

            time = curr_time
            visited.add(node)

            if node not in adj_list:
                continue

            for i, j in adj_list[node]:
                if i not in visited:
                    heapq.heappush(queue, (curr_time + j, i))

        if len(visited) != n:
            return -1
        else:
            return time