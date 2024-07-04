# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        new_value = 0
        while head.val != 0:
            new_value += head.val
            head = head.next

        next_node = self.mergeNodes(head.next)

        if new_value == 0:
            return next_node
            
        node = ListNode(new_value)
        node.next = next_node

        return node


