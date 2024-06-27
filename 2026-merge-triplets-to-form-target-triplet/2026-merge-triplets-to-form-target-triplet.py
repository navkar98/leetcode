class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = j = k = 0
        idx = 0
        n = len(triplets)
        
        while idx < n:
            curr_i = max(triplets[idx][0], i)
            curr_j = max(triplets[idx][1], j)
            curr_k = max(triplets[idx][2], k)

            # print(curr_i, curr_j, curr_k)

            if all([curr_i <= target[0], curr_j <= target[1], curr_k <= target[2]]):
                i = curr_i
                j = curr_j
                k = curr_k

        
            idx +=1

        if all([i == target[0], j == target[1], k == target[2]]):
            return True
        return False