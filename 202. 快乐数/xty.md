[toc]

---

### 1. 快乐数

![](https://i.loli.net/2019/12/28/RfAD9ynSZK3zkYH.jpg)

### 2. 思路

迭代次数，是我提交了好几次试出来的，当然可能更低，

### 3. 代码

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        #    迭代次数
        k = 0
        while n != 1:
            temp = 0
            str_n = str(n)
            for i in range(len(str_n)):
                temp += int(str_n[i])**2
            
            n = temp
            k+=1
            if k > 10:
                break
        
        return True if k <= 10 else False
```

