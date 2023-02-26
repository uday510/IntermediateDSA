# Given a binary tree, return the inorder traversal of its nodes' values.

# NOTE: Using recursion is not allowed.



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is root node of the binary tree, A.



# Output Format
# Return an integer array denoting the inorder traversal of the given binary tree.



# Example Input
# Input 1:

#    1
#     \
#      2
#     /
#    3
# Input 2:

#    1
#   / \
#  6   2
#     /
#    3


# Example Output
# Output 1:

#  [1, 3, 2]
# Output 2:

#  [6, 1, 3, 2]


# Example Explanation
# Explanation 1:

#  The Inorder Traversal of the given tree is [1, 3, 2].
# Explanation 2:

#  The Inorder Traversal of the given tree is [6, 1, 3, 2].

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def inorderTraversal(self, A):
        lst = []
        self.inorderTraversalRec(A,lst)
        return lst
    def inorderTraversalRec(self,A,lst):
        if A == None:
            return
        self.inorderTraversalRec(A.left,lst)
        lst.append(A.val)
        self.inorderTraversalRec(A.right,lst) 