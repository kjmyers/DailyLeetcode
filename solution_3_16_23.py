# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # root is last of postorder
        # find root in inorder
        # do the same for left and right of root
        # 
        graph = {}
        for i in range(len(inorder)):
            graph[inorder[i]] = i
        
        def func(start,end):
            curNode = TreeNode(postorder.pop())
            #print(curNode.val)
            curInd = graph[curNode.val]
            #print(curInd)

            if curInd < end-1: #Still nodes to right
                curNode.right = func(curInd+1,end)
            if curInd > start: #Still nodes to left
                curNode.left = func(start,curInd)
            
            return curNode
        
        return func(0,len(inorder))

        
        # val = pop postorder
        # Make treenode of val
        # Find val ind in inorder (graph)
        # pop next postorder
        # make treenode of val
        # find val ind
        # if ind is less than previous, attach to left
        # else attach to right
