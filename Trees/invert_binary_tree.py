# LeetCode 226 - Invert Binary Tree

# Approach 1: Recursive DFS
class SolutionRecursive:
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
    
# Approach 2: Iterative DFS using Stack
class SolutionDFS:
    def invertTree(self, root):
        if root is None:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

# Approach 3: BFS using Queue
from collections import deque

class SolutionBFS:
    def invertTree(self, root):
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root