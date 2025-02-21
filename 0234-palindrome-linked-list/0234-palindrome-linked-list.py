# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Find middle 
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse
        prev = None
        # E.g: 1--> 2--> 3--> 4 -->
        while slow:
            temp = slow.next # 2 --> 3 --> 4 -->
            slow.next = prev # 1 -->
            prev = slow # 1 -->
            slow = temp # 2 --> 3 --> 4 -->

        # Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        