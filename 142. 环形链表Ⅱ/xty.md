[toc]

---

### 1. 环形链表Ⅱ

![](https://i.loli.net/2019/12/30/18xMJkrQzh4j2dO.jpg)

### 2. 思路

和上一道题差不多，如果用O(n)的空间复杂度处理的花

如果想用O(1)的空间复杂度，可以使用快慢指针法，快指针走两步，慢指针走一半

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        ListNode_addr = []
        
        q = head
        
        while q != None:
            
            if q not in ListNode_addr:
                ListNode_addr.append(q)
            else:
                return q
            q = q.next
        return None
```

