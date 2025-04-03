# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the linked list in to two halves
        def split(head):
            fast,slow = head, head
            prev = None

            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next

            prev.next = None
            return head, slow

        # Merge two sorted linked list
        def merge(left, right):
            merged = ListNode()
            tail = merged
            
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left if left else right   
            return merged.next

        # Recursive Merge Sort  
        def merge_sort(node):
            if not node or not node.next:
                return node

            left_half, right_half = split(node)
            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)

            return merge(left_sorted, right_sorted)

        return merge_sort(head)



        

        