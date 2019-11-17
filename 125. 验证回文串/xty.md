[toc]

---

#### 1. 验证回文串

![](https://i.loli.net/2019/11/17/tJOVq2peBKkRXAn.jpg)

#### 2. 思路

**双指针**

首先将所有的英文字符修改为小写英文。设置两个指针，一个从前开始扫描，一个从后开始扫描，遇到英文字符或数字停止扫描，检测两个元素是否相同，相同则继续扫描，不同则返回False，

#### 3. 代码

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) <= 1:
            return True
        s = s.lower()
        pre, post = 0, len(s) - 1
        while pre<=post:
            while not s[pre].isalnum() and pre < post: pre += 1
            while not s[post].isalnum() and pre < post: post -= 1
            if s[pre] == s[post]:
                pre, post = pre + 1, post - 1
            else:
                return False
        return True
```

```
执行用时 :60 ms, 在所有 python3 提交中击败了79.21% 的用户
内存消耗 :14.2 MB, 在所有 python3 提交中击败了31.06%的用户
```







