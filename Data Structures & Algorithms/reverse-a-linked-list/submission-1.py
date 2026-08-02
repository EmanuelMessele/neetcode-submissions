# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we have the beginning of a singly linked list --> head
        # we want to return the beginning of the list but of a reversed linked list

        # implementation: 
        # we need a prev pointer so we have somewhere to point backwards
        # and a current to traverse the LL
        # replace current.next with prev flipping arrows --> then update prev and curr to go to next nodes in the list --> make sure to save link to next node in list
        # we will also need a nxt pointer to save our link to next curr

        # in the very end curr will be pointing at null and since prev is one behind it, it will be the last node, but technically the first in our reversed list

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
