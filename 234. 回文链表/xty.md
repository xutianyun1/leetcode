[toc]

---

### 1. 回文链表

![](https://i.loli.net/2019/12/31/dAyO5DmwheLfYrz.jpg)

### 2. 思路

先遍历一边链表，晓得该链表中共有多少个节点，然后第二遍扫描的时候，前一半节点将其存入一个列表中，后一半扫描中进行与列表中的元素比对，是否是回文。值得注意的是需要注意链表节点的数量为偶数还是奇数。

### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        first_half = []
        
        q = head
        Node_nums = 0
        while q != None:
            Node_nums += 1
            q = q.next
            
        if Node_nums == 1:
            return True
        q = head
        i = 1
        while q != None:
        
            if i <= Node_nums>>1:
                first_half.append(q.val)
                if i == Node_nums>>1:
                    #    奇数情况，需要跳过最中间的元素
                    if Node_nums%2 == 1:
                        i += 1
                        q = q.next
            else:
                if first_half[-1] != q.val:
                    return False
                first_half.pop()
            i += 1
            q = q.next
        return True
            
```

