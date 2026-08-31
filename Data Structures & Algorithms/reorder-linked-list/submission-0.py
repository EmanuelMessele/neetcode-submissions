# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # ==========================================
        # STEP 1: Find the middle of the linked list
        # ==========================================

        slow = head
        fast = head

        # slow moves 1 node at a time
        # fast moves 2 nodes at a time
        #
        # When fast reaches the end, slow will be
        # around the middle of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, slow is at the middle.
        #
        # Example:
        #
        # 1 -> 2 -> 3 -> 4 -> 5
        #          ^
        #        slow
        #
        # We want to split the list into:
        #
        # 1 -> 2 -> 3
        # 4 -> 5
        #
        # So we start reversing from slow.next.

        # ==========================================
        # STEP 2: Reverse the second half
        # ==========================================

        second = slow.next

        # Cut the first half off from the second half.
        #
        # This gives us:
        #
        # first:  1 -> 2 -> 3 -> None
        # second: 4 -> 5 -> None
        slow.next = None

        prev = None

        # Reverse the second half.
        #
        # Before:
        #
        # 4 -> 5 -> None
        #
        # After:
        #
        # 5 -> 4 -> None

        while second:
            # Save the next node before changing the pointer.
            temp = second.next

            # Reverse the direction of the pointer.
            second.next = prev

            # Move prev forward.
            prev = second

            # Move second forward using the saved node.
            second = temp

        # prev is now the head of the reversed second half.
        #
        # first half:
        # 1 -> 2 -> 3
        #
        # reversed second half:
        # 5 -> 4

        # ==========================================
        # STEP 3: Merge the two halves
        # ==========================================

        first = head
        second = prev

        # We now alternate between the two lists:
        #
        # first  -> second -> first -> second ...
        #
        # 1 -> 2 -> 3
        # 5 -> 4
        #
        # becomes:
        #
        # 1 -> 5 -> 2 -> 4 -> 3

        while second:
            # Save the next nodes because we're about
            # to change their pointers.
            temp1 = first.next
            temp2 = second.next

            # Connect first node to second node.
            first.next = second

            # Connect second node to the next first-half node.
            second.next = temp1

            # Move both pointers forward.
            first = temp1
            second = temp2



        

