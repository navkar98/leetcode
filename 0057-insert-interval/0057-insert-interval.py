class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        ans = []
        inserted = False

        for i in intervals:
            if not inserted and newInterval[0] < i[0]:
                ans.append(newInterval)
                ans[-1][1] = max(newInterval[1], ans[-1][1])
                inserted = True

            if not ans:
                ans.append(i)
            elif ans[-1][1] >= i[0]:
                ans[-1][1] = max(i[1], ans[-1][1])
            else:
                ans.append(i)

            if not inserted and ans[-1][1] >= newInterval[0]:
                ans[-1][1] = max(newInterval[1], ans[-1][1])
                inserted = True

        if not inserted:
            ans.append(newInterval)

        return ans
