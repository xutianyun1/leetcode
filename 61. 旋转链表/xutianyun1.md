[toc]

---

### 1. 旋转链表

![](https://i.loli.net/2020/01/02/Vh3tP9m7TBXcRn1.jpg)

### 2. 思路

将k对i求余得到k，然后将链表的后k个节点移动到表头

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        #    遍历链表得到链表长度
        q = head
        #    链表长度，每遍历一个+1
        i = 0
        while q != None:
            
            i += 1
            q = q.next
        #    将k对链表长度求余
        #    如果i==1或i==2,则直接返回head
        if i<2:
            return head
        #    因为如果k==i,则循环回原始状态
        k = k % i
        #    如果k==0,说明不需要移动任何元素
        if k == 0:
            return head

        q = head
        j = 0
        #    如果k==2,那么我们只需要将链表后2个移动到表头即可
        
        while j != i - k -1 :
            j += 1
            q = q.next
        #    获得后k个节点的第一个节点    
        r = q.next
        q.next = None
        
        q = r
        while q.next != None:
            q = q.next
        #    在后面接入前面的节点
        q.next = head
        
        return r
            
```

