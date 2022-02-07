from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, treeNode: Optional[TreeNode]) -> int:
        if not treeNode: return 0
        return max(self.getHeight(treeNode.left), self.getHeight(treeNode.right)) + 1

    def isBalanced(self, input: Optional[TreeNode]) -> bool:
        if not input: return True
        return self.isBalanced(input.left) and self.isBalanced(input.right) and abs(self.getHeight(input.left) - self.getHeight(input.right)) <= 1
      
Ex1 = TreeNode()
Ex1.val = 3
Ex1.left = TreeNode(val=9)
Ex1.right = TreeNode(val=20)
Ex1.right.left = TreeNode(val=15)
Ex1.right.right = TreeNode(val=7)

'''
An empty tree is height-balanced. A non-empty binary tree T is balanced if: 
1) Left subtree of T is balanced 
2) Right subtree of T is balanced 
3) The difference between heights of left subtree and right subtree is not more than 1. 

       0
    1    2
  3   3   
  

TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: None}}}

     0
  n     2
       3 3
'''

# [1,null,2,null,3]
# 
# --> heights = [2]
# max(heights) = 2
# min(heights) = 2


# [0, 1, 2, 3, 3] [0, 1, null, 3,3 ]
# def visit(self, treeNode, depth = 0)
#     if not left and not right: depth --> append
#     if left: visit(left, depth + 1)
#     if right: visit(right, depth + 1)

# isBalanced : return abs(max(hegiths) - min(heights)) <= 1

sol = Solution()
print(sol.isBalanced(Ex1)==True)
# print(sol.isBalanced([1,2,2,3,3,None,None,4,4])==False)