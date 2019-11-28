[toc]

---

### 1. 相交链表

![](https://i.loli.net/2019/11/28/h4mxqdVEDiHcN3J.jpg)

### 2. 思路

​	求两个链表的长度的差值，然后根据差值对两个链表进行对齐处理，再同时进行扫描链表，遇到相同的节点则返回，若到末尾节点也没有找到，则返回None。

​	对齐处理是指，若链表A比B长，则A先扫描长度的差值个节点。

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        q, p = headA, headB
        A_len = B_len = 0
        while q != None:
            A_len += 1
            q = q.next
        while p != None:
            B_len += 1
            p = p.next
        q, p = headA, headB
        red = A_len - B_len
        
        if red > 0:
            while red > 0:
                q = q.next
                red -= 1
        else:
            while red < 0:
                p = p.next
                red += 1
        
        while q!=None and p!=None:
            if p==q:
                return p
            q, p = q.next, p.next
            
        return None
```

### 4. 评论里的骚操作

```python

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        q, p = headA, headB
        
        while p!=q:
            p = p.next if p else headA
            q = q.next if q else headB
        
        return p
```

q,p同时扫描链表。q扫描完A扫描B，p扫描完B扫描A。弥补了链表A，B之间长度不一样，使得q，p扫描的节点数相同，则第二遍扫描时，若相交，则q==p