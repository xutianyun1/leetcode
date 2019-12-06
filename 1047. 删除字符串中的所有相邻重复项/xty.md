[toc]

---

### 1.  删除字符串中的所有相邻重复项

![](https://i.loli.net/2019/12/06/dnUwD9SmqGJivx1.jpg)

### 2. 思路

​		暴力啊，遍历由字符串转成的列表，如果下一个元素和当前元素相同，则删除这两个元素，并将index返回上一个元素，重新扫描。

### 3. 代码

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        index = 0
        re = list(S)
        print(re)
        while index < len(re)-1:
            
            if re[index] == re[index+1]:
                del re[index:index+2]

                index = index-1 if index-1 >= 0 else 0
            else:
                index+=1
        return ''.join(re)
```

### 4. 评论里的

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        #    栈
        stack = []
        
        for n in S:
            
            if stack and stack[-1] == n:
                stack.pop()
            else:
                stack.append(n)
        return ''.join(stack)
```

这道题 很明显是用栈的特性啊，wocao，我今天一定是被长春的风冻傻了



