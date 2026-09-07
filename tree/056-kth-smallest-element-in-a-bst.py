class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = 0

        def countlist(node):
            nonlocal count, answer
            if not node:
                return

            countlist(node.left)
            count += 1
            if count == k:
                answer = node.val
                return
            countlist(node.right)

        countlist(root)
        return answer
