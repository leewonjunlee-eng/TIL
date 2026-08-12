class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(node, depth):
            if not node:
                return

            if len(answer) < depth + 1:
                answer.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return answer
