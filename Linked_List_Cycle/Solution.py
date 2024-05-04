class Solution:
    def hasCycle(self, head) -> bool:
        """
        type head: Optional[ListNode]
        rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
