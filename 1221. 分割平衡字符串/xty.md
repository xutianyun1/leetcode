[toc]

---

### 1. 完美分割字符串

![](https://i.loli.net/2020/01/02/Vh3tP9m7TBXcRn1.jpg)

### 2. 思路

用栈来操作，初始时栈为空，将第一个元素入栈，指向下一个元素，记为当前元素，如果当前元素也栈顶元素相同，则将当前元素入栈，否则，将栈顶元素弹出，并检查栈是否为空栈，如果为空，则re+1.

### 3. 代码

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        #    栈
        stack = []
        
        re = 0
     
        for i in range(len(s)):
       
            if len(stack) == 0:
                #   如果栈空，则将当前元素入栈
                stack.append(s[i])
            else:
                if s[i] == stack[-1]:
                    #    如果当前元素与栈顶元素相同，则将当前元素入栈
                    stack.append(s[i])
                else:
                    #    否则栈顶元素出栈
                    stack.pop()
                    if len(stack) == 0:
                        re += 1
        return re
```

