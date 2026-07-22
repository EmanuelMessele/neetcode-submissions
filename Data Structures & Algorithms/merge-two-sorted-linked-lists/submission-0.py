# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we have 2 sorted linked lists
        # we need to merge them into one sorted linked list and return the head of this one linked list

        # implementation:
        # between both lists, we find the head that is smaller and follow that one
        # from there we traverse, whichever one is smaller we make that our next node and continue to traverse

        dummy = ListNode()      # placeholder node; its .next will be the real head
        tail = dummy            # always points at the last node in the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1       # link the smaller node in
                list1 = list1.next      # advance that list
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next            # the node we just linked is the new tail

        # exactly one list can still have nodes left — attach the whole rest at once
        tail.next = list1 if list1 else list2

        return dummy.next



        