[toc]

---

### 1. 路径总和

难度简单264收藏分享切换为英文关注反馈给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1


返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 2. 思路

前向遍历求和，用栈存取访问过的值，记得弹出

### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def formPath(self, root, N, path_sum):
        if root is None:
            return False
        path_sum.append(root.val)
        if root.left is None and root.right is None and N==sum(path_sum):
            return True
        
        if self.formPath(root.left, N, path_sum):
            return True
        if self.formPath(root.right, N, path_sum):
            return True
        if len(path_sum)!=0:
            path_sum.pop()
        return False
    def hasPathSum(self, root: TreeNode, N: int) -> bool:
        
        return self.formPath(root, N, [])
```

### 4. 别人的代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, N):
        
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return N - root.val == 0
        
        return self.hasPathSum(root.left, N-root.val) | self.hasPathSum(root.right, N-root.val)
```

整体思路差不多

都是前序遍历，但是核心就是他是逐个相减，判断减到叶子节点是是否为零。