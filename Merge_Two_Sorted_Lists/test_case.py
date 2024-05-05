import unittest
from Solution import Solution, ListNode


class MergeTwoLists(unittest.TestCase):
    def create_linked_list(self, values):
        head = last_node = None
        nodes = []

    def create_linked_list(self, values):
        head = last_node = None
        for value in values:
            new_node = ListNode(value)
            if not head:
                head = new_node
            if last_node:
                last_node.next = new_node
            last_node = new_node
        return head

    # If you're trying to compare two linked list objects directly using assertEqual, which checks if both objects are the same instance, not if they contain the same sequence of values. Since mergeTwoLists returns a new linked list, its instances will not be the same as the one created in your test, even if they contain identical values.
    
    def list_equal(self, list1, list2):
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 == None and current2 == None
    
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for list1, list2, expected_result in [([1,2,4], [1,3,4], [1,1,2,3,4,4]),
                                     ([], [], []),
                                     ([], [0], [0])]:
            
            l1 = self.create_linked_list(list1)
            l2 = self.create_linked_list(list2)
            result = s.mergeTwoLists(l1, l2)
            expected_result = self.create_linked_list(expected_result)
            self.assertTrue(self.list_equal(result, expected_result))

if __name__ == "__main__":
    unittest.main()