class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        last = []
        intervals.sort()
        
        for i in intervals:
            if last and last[-1][1] > i[0]:
                last[-1][1] = min(last[-1][1], i[1])
            else:
                last.append(i)

        return len(intervals) - len(last)