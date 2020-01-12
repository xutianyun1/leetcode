[toc]

---

### 1. 相同的树

![1578839251006](C:\Users\xutia\AppData\Roaming\Typora\typora-user-images\1578839251006.png)

### 2. 思路

通过对树进行层次遍历将树的链式存储转为线性存储，判断两个数组是否相等即可。

### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    
    def get_node(self, root):
        if root == None:
            return []
        #    创建队列
        q = Queue()
        #    存放节点的列表
        node = []
        #    根节点入队
        q.put(root)
        node.append(root.val)
        
        while not q.empty():
            #    出队
            r = q.get()
            if r.left != None:
                q.put(r.left)
                node.append(r.left.val)
            else:
                node.append(None)
            if r.right != None:
                q.put(r.right)
                node.append(r.right.val)
            else:
                node.append(None)
        
        return node
            
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        return self.get_node(p) == self.get_node(q)

    

```

