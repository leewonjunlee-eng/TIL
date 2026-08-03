from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur1 = list1
        cur2 = list2
        now = dummy

        while cur1 and cur2:
            if cur1.val >= cur2.val:
                now.next = cur2
                now = cur2
                cur2 = cur2.next
            else:
                now.next = cur1
                now = cur1
                cur1 = cur1.next

        now.next = cur1 or cur2
        return dummy.next


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(values):
        head = None
        for value in reversed(values):
            head = ListNode(value, head)
        return head

    def values(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()
    assert values(solution.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert values(solution.mergeTwoLists(None, build([0]))) == [0]
