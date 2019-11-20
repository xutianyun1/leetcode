[toc]

---

### 1. 合并两个有序链表

![](https://i.loli.net/2019/11/20/ODxqLw1TgMmeSo6.jpg)

### 2. 思路

​		普通的链表应用问题，这个问题不大，大的问题是python对于链表的实现 我还不是特别熟练。

​		先创建一个新的链表，建立哨兵节点。对l1和l2进行遍历，比较val的值。将较小的值的节点加入到新的链表中。

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        q, p = l1, l2
        
        res = ListNode(None)
        node = res
        
        while q and p:
            if q.val < p.val:
                node.next = q                
                q = q.next
            else:
                node.next = p
                p = p.next
            node = node.next
        
        if q:
            node.next = q
        else:
            node.next = p
        
        return res.next
            
```

