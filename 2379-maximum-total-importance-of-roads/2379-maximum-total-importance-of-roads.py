class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counts = collections.defaultdict(int)

        for u, v in roads:
            counts[u]+=1
            counts[v]+=1

        weights = collections.defaultdict(int)
        weight = n
        for i in [(k, v) for k, v in sorted(counts.items(), key=lambda item: -item[1])]:
            weights[i[0]] = weight
            weight -= 1
        
        ans = 0

        for u, v in roads:
            ans += weights[u]
            ans += weights[v]

        return ans
