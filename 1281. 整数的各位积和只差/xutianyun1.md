[toc]

---

### 1. 整数的各位积和之差

![](https://raw.githubusercontent.com/xutianyun1/cloudimage/master/img/1281.png)



### 2. 思路

属实简单

### 3. 代码

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        temp = 0
        sum_n = 0
        product = 1
        while n >= 1:
            temp = int(n%10)
            n = n/10
            sum_n += temp
            product *= temp
        return product-sum_n
```

