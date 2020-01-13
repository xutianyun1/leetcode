[toc]

---

### 1. 猜数字

![1578927848794](C:\Users\xutia\AppData\Roaming\Typora\typora-user-images\1578927848794.png)

### 2. 思路

遍历检测两个数组有几个在同一位置上的元素相同就完事了啊。好久没做这么简单的题，我都有点懵了。

### 3. 代码

```python
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        
        guess_number = 0
        for i in range(len(guess)):
            
            if guess[i] == answer[i]:
                guess_number += 1
                
        return guess_number
```

