# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list:
            return None
        
        heap = []
        sorted_list = ListNode(0)
        cur = sorted_list

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i , node))

        while heap:
            min_num, index, node = heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heappush(heap, (node.next.val, index, node.next))

        return sorted_list.next


        