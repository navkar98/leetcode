class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # print(len(range(int(sqrt(c)/2) + 1)))
        # return False

        for i in range(int(sqrt(c)) + 1):
            sub = c - int(math.pow(i,2))
            # print(sub)
            temp = isqrt(sub)
            if math.pow(temp,2) == sub:
                return True
        
        return False

