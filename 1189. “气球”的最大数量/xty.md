[toc]

---

### 1. “气球”的最大数量

![](https://i.loli.net/2019/12/23/t6xbGMU3nCImkgE.jpg)

### 2. 思路

暴力了又是， 每次while循环检测的是是否有一个“气球”，内层for循环检测的是text中是否还有一个"气球"，具体的，遍历word的字符，检测该字符是否在text中，如果在则将该字符从text中删除，如果遍历完word字符，并没有return，说明text中至少具备一个word，此时将word_nums+1。如果该遍历的字符在text中找不到，则return word_nums

### 3. 代码

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        word = 'balloon'
        
        cnt = True
        word_nums = 0
        while cnt:
            
            for n in word:
                if n in text:
                    text = text.replace(n,'',1)
                else:
                    return word_nums
            word_nums += 1
            
```

