```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
            
        while head.next and head.val != None:
            head.val = None
            head = head.next
        
        if not head.next:
            return False
        
        return True
```


### 遍历链表，将val置空，遇到下一个val为空时判断是不是最后一个，是则False 否则True

##### 执行用时 :52 ms, 在所有 python3 提交中击败了85.51%的用户
##### 内存消耗 :15.7 MB, 在所有 python3 提交中击败了100.00%的用户

