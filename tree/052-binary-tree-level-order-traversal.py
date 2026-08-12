class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def dfs(node, depth):
            if not node:
                return

            if len(answer) < depth + 1:
                answer.append([node.val])
            else:
                answer[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return answer
