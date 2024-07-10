class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            if i == "../" and stack:
                stack.pop()
            elif i == "./" or i == "../":
                continue
            else:
                stack.append(i)

        return len(stack)