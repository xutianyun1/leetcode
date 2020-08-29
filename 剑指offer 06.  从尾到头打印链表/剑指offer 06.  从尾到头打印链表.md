#### 1. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

**示例 1：**

```
输入：head = [1,3,2]
输出：[2,3,1]
```



#### 2. 思路

创建一个数组，遍历链表，依次将链表元素添加到数组中，返回数组的倒序结果

#### 3. 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        count = []
        p = head
        while p != None:
            count.append(p.val)
            p = p.next
        return count[::-1]
```

#### 4. 递归的思路

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    __count = []
    def __init__(self):
        self.__count = []

    def helpme(self, p):
        if p is None:
            return
        self.helpme(p.next)
        self.__count.append(p.val)


    def reversePrint(self, head: ListNode) -> List[int]:

        self.helpme(head)
        return self.__count

```

