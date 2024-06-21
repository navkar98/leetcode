from functools import cache

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        iter_dict = {}
        ans = []
        stack = ["JFK"]
        n = len(tickets)

        for dep, arr in tickets:
            if dep not in iter_dict:
                iter_dict[dep] = [arr]
            else:
                iter_dict[dep].append(arr)

        for key in iter_dict.keys():
            iter_dict[key].sort(reverse=True)

        while stack:
            top = stack[-1]

            if top in iter_dict and len(iter_dict[top]) > 0:
                stack.append(iter_dict[top].pop())
            else:
                ans.append(stack.pop())

        return ans[::-1]