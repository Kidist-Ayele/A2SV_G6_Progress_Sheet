# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            new_node = ListNode(total % 10)
            temp.next = new_node
            temp = temp.next
            carry = total // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            new_node = ListNode(total % 10)
            carry = total // 10
            temp.next = new_node
            temp = temp.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            new_node = ListNode(total % 10)
            carry = total // 10
            temp.next = new_node
            temp = temp.next
            l2 = l2.next
            
        if carry > 0:
            new_node = ListNode(carry)
            temp.next = new_node

    
        
        return dummy.next
         


