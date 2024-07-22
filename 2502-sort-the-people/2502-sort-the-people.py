class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [j for i, j in sorted(zip(heights, names))][::-1]