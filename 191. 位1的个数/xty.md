[toc]

---

### 1. 位1的个数

![](https://i.loli.net/2019/12/24/4rlHSe1Vqxa5zo6.jpg)

### 2. 思路

一眼就出答案啊，先转成二进制字符串，然后对这个字符串中的字符’1‘计数。

### 3. 代码

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n)[2:].count('1')

```



### 4 . 题解

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while n != 0:
            
            count += n&1
            n = n>>1
        return count
```



将n和1进行与运算，结果是n的最低位，然后对n进行右移一位，这样，对n的每一位位数上的值进行累加，便是1的个数