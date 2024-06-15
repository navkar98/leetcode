class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []

        projects_count = pointer = 0
        n = len(profits)

        profits_and_capital = sorted(list(zip(capital, profits)))

        while projects_count < k:
            while pointer < n and w >= profits_and_capital[pointer][0]:
                heapq.heappush(heap, -profits_and_capital[pointer][1])
                pointer += 1

            if not heap:
                break

            projects_count += 1
            w += (-heapq.heappop(heap))

        return w