# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        left_dummy = ListNode()
        right_dummy = ListNode()

        left, right = left_dummy, right_dummy
        current = head

        while current:
            if current.val < x:
                left.next = current
                left = left.next

            else:
                right.next = current
                right = right.next
            current = current.next

        right.next = None
        left.next = right_dummy.next
        return left_dummy.next

        