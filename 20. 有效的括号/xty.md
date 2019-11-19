[toc]

---

### 1. 有效的括号

![](https://i.loli.net/2019/11/19/2XrwM1jSuCEZB4g.jpg)

### 2. 思路

​		括号的匹配是一个栈的应用问题：从头开始扫描字符串，遇到**左括号**便使其进栈，遇到**右括号**便检测栈顶元素是否与其匹配，若匹配则继续扫描，不匹配则直接返回False。

 		Note: 

1. 注意一些边界条件，例如，如果遇到**右括号**，但**栈长度为0**，即栈内**无左括号**，则返回False。

2. 从头到尾扫描完字符串后，如果括号都是有效的，栈应为**空**。

### 3. 代码

```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        #    栈    
        stack = []
        #    右括号符号与之匹配的左括号符合
        right_dict = {')': '(',
                      '}': '{',
                      ']': '['}
        #    左括号符号列表
        left = right_dict.values()
        for n in s:
            
            if n in left:
                #    进栈
                stack.append(n)
            else:
                #    检查栈顶元素是否匹配
                if len(stack) == 0 or right_dict[n] != stack.pop():
                    return False

        return True if len(stack) == 0 else False
```

```
执行用时 :32 ms, 在所有 python3 提交中击败了99.15%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.51%的用户
```

### 4. 评论里的骚操作

```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')
        return s == ''
```

如果字符串是有效括号，那么就像解套一样，将匹配的括号挨个消去。最终字符串为空，返回True。如果不匹配 最终字符串不会为空，返回False。骚操作的确是骚操作，但性能下降了不少。