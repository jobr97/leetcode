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
                current.val = (l1.val + l2.val + carry) % 10
                carry = int((l1.val + l2.val + carry) / 10)
                if carry == 1:
                    current.next = ListNode()
                    current.next.val = 1
                return first
            current.val = (l1.val + l2.val + carry) % 10
            carry = int((l1.val + l2.val + carry) / 10)
            current.next = ListNode()
            current = current.next
            if not l1.next:
                l1 = ListNode()
            else:
                l1 = l1.next
            if not l2.next:
                l2 = ListNode()
            else:
                l2 = l2.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    l2 = ListNode(9)
    node = s.addTwoNumbers(l1, l2)
    print(f"[{node.val}", end="")
    node = node.next
    while node:
        print(f",{node.val}", end="")
        node = node.next
    print("]")
