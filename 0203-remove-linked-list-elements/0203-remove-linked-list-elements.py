# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        itr = prev.next
        
        def removeElement(itr, prev):
            if not itr:
                return 

            if itr.val == val:
                prev.next = itr.next
                removeElement(prev.next, prev)
            else:
                removeElement(itr.next, itr)
            
        removeElement(dummy.next, dummy)
        return dummy.next
        
            


        