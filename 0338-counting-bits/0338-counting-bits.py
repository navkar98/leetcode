class Solution:
    def countBits(self, n: int) -> List[int]:
        order = 1
        counter = 0
        ans = [0] * (n+1)

        for i in range(1, n+1):
            if i == 2**order:
                order+=1
                counter = 0
            ans[i] = ans[counter] + 1
            counter += 1
        
        return ans