class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0

        def dfs(node, max):
            nonlocal answer
            if not node:
                return

            if node.val >= max:
                answer += 1
                max = node.val
            dfs(node.left, max)
            dfs(node.right, max)

        dfs(root, -1000)
        return answer
