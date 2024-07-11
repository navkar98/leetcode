class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [] 
        tmp = ''

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(tmp)
                tmp = ''
            elif s[i] == ')':
                tmp = tmp[::-1]
                tmp = stack.pop() + tmp
            else:
                tmp += s[i]

        stack.append(tmp)
        return ''.join(stack)