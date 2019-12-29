[toc]

---

### 1. 二进制间距

![](https://i.loli.net/2019/12/29/2CPm8VbgUAGlRqO.jpg)



### 2. 思路

先将其转为二进制字符串，然后在二进制字符串中寻找第一个为‘1’的字符，记录此时的下标，从该下标开始遍历二进制字符串，如果遇到下一个为‘1’的字符，则进行比较此时两个连续为1的距离是否比已知的最大距离要大。

### 3. 代码

```python
class Solution:
    def binaryGap(self, N: int) -> int:
        
        N_bin = bin(N)
        
        max_dist = 0

        pre = N_bin.find('1')
        if pre == -1:
            return 0
        for i in range(pre, len(N_bin)):
            
            if N_bin[i] == '1':
                max_dist = max(max_dist, i - pre)
                pre = i
        
        return max_dist
```



