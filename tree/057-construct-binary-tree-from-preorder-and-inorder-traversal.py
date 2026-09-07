class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        inorder_map = {
            value: index
            for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(inorder_left, inorder_right):
            nonlocal preorder_index

            if inorder_left > inorder_right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            root_index = inorder_map[root_value]

            root.left = build(
                inorder_left,
                root_index - 1
            )

            root.right = build(
                root_index + 1,
                inorder_right
            )

            return root

        return build(0, len(inorder) - 1)
