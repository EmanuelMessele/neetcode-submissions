# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we are given the head of a linked list
        # if there is cycle meaning, we visit the same node more than once, then return true, if not return false. 

        # can we not just put every node visited into a set
        # if it sees the same node as we contiue trying to reach null, then we can return true

        current = head
        nodes = set()
        
        while current:
            if current in nodes:
                return True
        
            nodes.add(current)

            current = current.next
        
        return False

