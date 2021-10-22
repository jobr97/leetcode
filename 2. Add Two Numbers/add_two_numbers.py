from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode()
        current = first
        carry = 0
        while True:
            if not l1.next and not l2.next:
                return first
            else:
                return first


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    node = s.addTwoNumbers(l1, l2)
    print(f"[{node.val}", end="")
    while node.next:
        print(f",{node.val}", end="")
    print("]")
