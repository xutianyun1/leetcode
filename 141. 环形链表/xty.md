[toc]

---

### 1. 环形链表

![](https://i.loli.net/2019/12/30/r1QMEDSUulxmZKs.jpg)

### 2. 思路

建立一个列表用于存储访问过的节点，如果当前正在访问的节点已经在列表中存储。表明是环形链表

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        ListNode_addr = []
        
        q = head
        
        cnt = True
        
        while q is not None:
            if q not in ListNode_addr:
                
                ListNode_addr.append(q)
            else:
                return True
            q = q.next
        return False
            
            
```

