# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first = mid = last = head
        # Find medium 
        while last and last.next:
            mid = mid.next
            last = last.next.next

        # Reverse
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        # Find maximum twin sum
        max_val = 0
        while first and prev:
            max_val = max(max_val, first.val + prev.val)
            first = first.next
            prev = prev.next

        return max_val

        