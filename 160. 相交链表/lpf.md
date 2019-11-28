    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    
            p = headA
            q = headB
            while p!=q:
                p = p.next if p else headB
                q = q.next if q else headA
            return p 
            
            
            
### 链表操作还是不熟，代码是抄的神思路，服了,成绩就不贴了，大搞速度超过90%