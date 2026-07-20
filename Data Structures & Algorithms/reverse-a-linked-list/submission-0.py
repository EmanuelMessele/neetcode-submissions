# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we have the beginning of a linked list
        # return the beginning of a reversed linked list

        # implementation:
        prev = None
        curr = head

        while curr:
            nxt = curr.next    # 1. save the rest of the list before we cut it off
            curr.next = prev   # 2. flip the arrow backwards
            prev = curr        # 3. advance: current node is now the "reversed part's head"
            curr = nxt         # 4. advance: move on to what used to be next

        return prev


