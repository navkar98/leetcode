class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        non_grumpy = 0
        n = len(customers)

        for i in range(n):
            if grumpy[i] == 0:
                non_grumpy += customers[i]
                customers[i] = 0
        
        window = sum(customers[:minutes]) + non_grumpy
        ans = window
        
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                window -= customers[i - minutes]
            
            if grumpy[i] == 1:
                window += customers[i]

            ans = max(ans, window)

        return ans