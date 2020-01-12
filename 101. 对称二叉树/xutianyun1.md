[toc]

---

### 1. 对称二叉树

### 2. 思路

### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    
    def func(self, node1, node2):
        if node1 != None and node2 != None:
          
            if node1.val != node2.val:
                return False
            elif self.func(node1.left, node2.right) and self.func(node1.right, node2.left):
                return True       
        elif node1 == None and node2 == None:
            return True
        else:
            return False
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        if self.func(root.left, root.right) == 1:
            return True
        else:
            return False
      
            
        
        
            
                
                
```

