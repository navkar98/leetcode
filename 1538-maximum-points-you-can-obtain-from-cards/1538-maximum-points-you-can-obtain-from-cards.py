class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        sumFromStart = []
        sumFromEnd = []

        for i in cardPoints:
            if not sumFromStart:
                sumFromStart.append(i)
            else:
                sumFromStart.append(i + sumFromStart[-1])

        for i in cardPoints[::-1]:
            if not sumFromEnd:
                sumFromEnd.append(i)
            else:
                sumFromEnd.append(i + sumFromEnd[-1])

        for i in range(k+1):
            if i == 0:
                ans = max(ans, sumFromStart[k-1])
            elif i == k:
                ans = max(ans, sumFromEnd[k-1])
            else:
                ans = max(ans, sumFromStart[k-i-1] + sumFromEnd[i-1])
            # print(i, ans)
        return ans