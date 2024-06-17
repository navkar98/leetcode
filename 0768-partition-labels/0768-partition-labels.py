class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chrs = {}
        idx = 0

        for i in s:
            if i not in chrs:
                chrs[i] = [idx, idx]
            else:
                chrs[i][1] = idx

            idx += 1

        intervals = sorted(list(chrs.values()))
        idx = 0
        new_interval = []

        while idx < len(intervals):
            if not new_interval or (new_interval and new_interval[-1][1] < intervals[idx][0]):
                new_interval.append(intervals[idx])
            else:
                new_interval[-1][1] = max(intervals[idx][1], new_interval[-1][1])
            idx+=1

        return [i[1] - i[0] + 1 for i in new_interval]