# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = last_node = ListNode()

        def reverseNode(head_node):
            prev = None
            while head_node:
                next_node = head_node.next
                head_node.next = prev
                prev = head_node
                head_node = next_node
            return prev

        while head:
            count = 0
            first_node = head
            
            while head:
                count += 1
                next_node = head.next
                if count == k:
                    head.next = None
                    head = next_node
                    break
                head = next_node

            if count == k:
                reverse_head = reverseNode(first_node)
                last_node.next = reverse_head
                last_node = first_node
            else:
                last_node.next = first_node

        return dummy_node.next





        