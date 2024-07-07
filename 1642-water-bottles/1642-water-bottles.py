class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        while ((numBottles + empty) // numExchange) > 0 or numBottles >= numExchange:
            # print(numBottles, empty)
            ans += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty -= numBottles * numExchange
        
            # print(numBottles, empty)
        return ans + numBottles