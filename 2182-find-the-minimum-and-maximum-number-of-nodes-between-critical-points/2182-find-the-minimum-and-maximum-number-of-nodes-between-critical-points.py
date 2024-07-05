# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(first, curr, second):
            if first and first.val < curr.val and second and second.val < curr.val:
                return True
            if first and first.val > curr.val and second and second.val > curr.val:
                return True

        ans = [inf, -inf]
        firstCritical = 0
        lastCritical = 0
        counter = 0

        prev = None
        while head:
            counter += 1
            if isCritical(prev, head, head.next):
                if firstCritical == 0:
                    firstCritical = counter
                
                if lastCritical != 0:
                    ans[0] = min(ans[0], counter - lastCritical)

                lastCritical = counter

            prev = head
            head = head.next

        
        if firstCritical == lastCritical or ans == [inf, -inf]:
            return [-1, -1]
        else:
            ans[1] = lastCritical - firstCritical
            return ans