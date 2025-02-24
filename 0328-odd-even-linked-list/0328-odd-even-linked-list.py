# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy_node = ListNode()
        dummy_node.next = head

        if not head.next:
            return head

        even_node = last_node = head.next

        while last_node and last_node.next:

            next_node = last_node.next
            head.next = next_node
            last_node.next = next_node.next
            last_node = last_node.next
            head = head.next
    
        head.next = even_node
        return dummy_node.next
        