class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered_heights = sorted(heights)
        ans = 0

        for i, j in zip(heights, ordered_heights):
            if i != j:
                ans += 1

        return ans