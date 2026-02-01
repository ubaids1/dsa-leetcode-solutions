# LeetCode 226 - Invert Binary Tree
# Recursive DFS solution

class Solution:
    def invertTree(self, root):
        # Step 1: base case
        if root is None:
            return None

        # Step 2: swap children
        root.right, root.left = root.left, root.right

        # Step 3: invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Step 4: return root
        return root