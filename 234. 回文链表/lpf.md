```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]
```

### 简单粗暴的方法

##### 执行用时 :68 ms, 在所有 python3 提交中击败了95.24%的用户
##### 内存消耗 :23.1 MB, 在所有 python3 提交中击败了99.47%的用户



