将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4


    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 首先实例化一个链表
        res = ListNode(None)
        node = res

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


### 第一次接触python的链表，一脸懵逼，啥都不会，学习为主

##### 执行用时 : 60 ms, 在所有 python3 提交中击败了34.18%的用户
##### 内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.66%的用户