[toc]

---

### 1. 二进制表示中质数个计算置为

![](https://i.loli.net/2019/12/02/xjKZkabCvoAdti2.jpg)

### 2. 思路

​		这道题蛮简单的，就是暴力就完事了。

​        优化的话，就是可以先把小于32的整数的质数存在一个列表中，直接检查1的个数是否在列表中。

### 3. 代码

```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        #    返回结果
        num = 0
        for n in range(L, R+1):
            #    转为二进制字符串
            bin_str = bin(n).replace('0b', '')
            #    转为列表然后计算字符'1'的个数
            m = list(bin_str).count('1')
            #    如果m==1则终止本次循环，继续下次循环
            if m==1:
                continue
            #    判断是否是素数
            i = 2
            while i<m**0.5:
                '''
                判断是不是素数
                '''
                if m%i == 0:
                    break
                i+=1
            #    如果i>m**0.5说明m是质数   
            if i>m**0.5:
                num+=1
        return num
                    
```

