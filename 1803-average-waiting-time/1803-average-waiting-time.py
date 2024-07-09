class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_order_time = 0
        wait_time = []

        for arr, time in customers:
            curr_order_time = max(curr_order_time, arr) + time
            wait_time.append(max(0, curr_order_time - arr))

        return sum(wait_time)/len(wait_time)