class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        times = time % ((n * 2) - 2)

        if times >= n:
            return n - (times - n + 1)
        else:
            return times + 1
