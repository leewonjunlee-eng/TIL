class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            diameter = max(diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return diameter
