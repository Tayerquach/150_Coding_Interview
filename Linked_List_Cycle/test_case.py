import unittest
from Solution import Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListCycle(unittest.TestCase):
    def create_linked_list_with_cycle(self, values, pos):
        head = last_node = None
        nodes = []
        
        for value in values:
            new_node = ListNode(value)
            nodes.append(new_node)
            if not head:
                head = new_node
            if last_node:
                last_node.next = new_node
            last_node = new_node

        # Creating a cycle
        if pos != -1:
            last_node.next = nodes[pos]
        
        return head
    
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        
        for values, pos, result in [([3,2,0,-4], 1, True),
                                    ([1,2], 0, True),
                                    ([1], -1, False)]:
            head = self.create_linked_list_with_cycle(values, pos)
            self.assertEqual(s.hasCycle(head), result)
    
if __name__ == "__main__":
    unittest.main()
