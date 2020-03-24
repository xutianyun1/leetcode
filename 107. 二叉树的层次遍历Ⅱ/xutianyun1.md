[toc]

---

####  1. 二叉树的层次遍历Ⅱ

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 2. 思路

就是简单的层次遍历，但是需要根据计数的每层节点数来进行区分进入到下一层。

#### 3. 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Solution:
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        re = []    
        q = queue.Queue()
        if root is None:
            return []
        q.put(root)
        #    当前层未遍历的节点数
        level_num = 1
 		#    下一层节点数
        next_level_num = 0
        temp = []
        while not q.empty():
            r = q.get()
            temp.append(r.val)
            level_num -= 1
            
            if r.left is not None:
                q.put(r.left)
                next_level_num += 1
            if r.right is not None:
                q.put(r.right)
                next_level_num += 1
            #    如果当前层未遍历的节点数为零，说明下一个节点进入到下一层，此时做特定处理  
            if level_num == 0:
                re.append(temp)
                temp = []
                level_num = next_level_num
                next_level_num = 0
                        
        return re[::-1]
```



