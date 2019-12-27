[toc]

---

### 1. 叶子相似的树

![](https://i.loli.net/2019/12/27/we5mpTO1rDYRtMu.jpg)

### 2. 思路

so easy。首先对树进行前序遍历，在遍历过程中将叶子节点存入一个列表中，最后检查两个列表是否相等。

### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def pre_traversal(self, node, leaf_node):
        '''
        对二叉树进行前序遍历
        node[TreeNode]: 二叉树的根节点
        leaf_node[List]:二叉树的叶节点从左到右排序
        '''
        if node is None:
            return
        self.pre_traversal(node.left, leaf_node)
        self.pre_traversal(node.right, leaf_node)
        if node.left is None and node.right is None:
            leaf_node.append(node.val)

        
        return leaf_node
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_node1 = []
        leaf_node2 = []
        import operator
        print(self.pre_traversal(root1, leaf_node1), self.pre_traversal(root2, leaf_node2))
        
        return operator.eq(leaf_node1, leaf_node2)
        
        
```

