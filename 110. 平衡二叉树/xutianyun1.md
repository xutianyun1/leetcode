[toc]

---

  ### 1. 平衡二叉树

难度简单276收藏分享切换为英文关注反馈给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：


一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。


示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    	3
       / \
      9  20
        /  \
       15   7


返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4



返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 2. 思路

递归求树高，顺便就求了是否是平衡二叉树

### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def treeHigh(self, root):
        
        if root is None:
            return 0, True
        if root.left is None and root.right is None:         
            return 1, True
        
        left, is_balanced1 = self.treeHigh(root.left)
        right, is_balanced2 = self.treeHigh(root.right)
        print(left, right)
        return max(left,right) + 1, (abs(left - right) <= 1) & is_balanced1 & is_balanced2
    
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        _, is_balanced = self.treeHigh(root)
        return is_balanced
```

