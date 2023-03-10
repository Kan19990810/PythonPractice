"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None
        cur = root
        while cur:
            parent = cur
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root