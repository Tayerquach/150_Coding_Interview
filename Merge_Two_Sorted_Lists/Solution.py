class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val} -> {self.next}"
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        type list1: ListNode
        type list2: ListNode
        rtype: ListNode
        """

        current = dummy = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next



