class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = collections.defaultdict(list)

        for f, t, w in edges:
            adj[f].append((t, w))
            adj[t].append((f, w))

        def get_max_connections(node):
            heap = [(distanceThreshold, 0, node)]
            max_conn = 0
            visited = set()
            # print(node)

            while heap:
                dist_avail, count, curr_node = heapq.heappop(heap)
                dist_avail = abs(dist_avail)

                max_conn = max(max_conn, count)
                visited.add(curr_node)

                for t, w in adj[curr_node]:
                    if t not in visited and w <= dist_avail:
                        heapq.heappush(heap, (-(dist_avail - w), count + 1, t))

                # print(visited)
            return len(visited) - 1

        # print(adj)
        counts = []
        for i in range(n):
            counts.append((get_max_connections(i), i))
        # print(counts)
        return sorted(counts, key = lambda i: (i[0], -i[1]))[0][1]

