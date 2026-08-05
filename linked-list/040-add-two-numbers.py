from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        left = l1
        right = l2
        carry = 0

        while left or right or carry:
            total = carry

            if left:
                total += left.val
                left = left.next
            if right:
                total += right.val
                right = right.next

            tail.next = ListNode(total % 10)
            tail = tail.next
            carry = total // 10

        return dummy.next


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(values):
        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next

    def values(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()
    assert values(solution.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert values(solution.addTwoNumbers(build([9, 9]), build([1]))) == [0, 0, 1]
