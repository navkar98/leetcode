class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []

        if x > y:
            pref = "ab"
            sec = "ba"
        else:
            pref = "ba"
            sec = "ab"
            x, y = y, x 
        
        ans = 0
        for i in s:
            if stack and stack[-1] + i == pref:
                ans += x
                stack.pop()
            else:
                stack.append(i)
        
        s = "".join(stack)
        stack = []
        for i in s:
            if stack and stack[-1] + i == sec:
                ans += y
                stack.pop()
            else:
                stack.append(i)

        return ans
