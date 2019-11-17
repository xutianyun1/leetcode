[toc]

---

### 1. 爬楼梯

![](https://i.loli.net/2019/11/17/MxOymJhbq1TucSr.jpg)



### 2. 思路

​	简单的动态规划。到达第二个阶梯有1种方法（从第一个阶梯到第二个阶梯）；到达第三个阶梯有2种方法（从第一阶梯上去或者从第二个阶梯上去）；到达第四个阶梯有两种方法（从第二个阶梯上去或者从第三个阶梯上去）。

​	假定F1表示第一个阶梯的方案，F2表示到达第二个阶梯的方案，F3表示到达第三个阶梯的方案。因此有，

​											F3 = F2 + F1

​											F4 = F3 +  F2

​													···

​											Fn = Fn-1 + Fn-2

​	有点像斐波那契数列。

### 3. 代码

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        
        fc = [0]*(n+1)
        fc[0] = 1
        fc[1] = 1
        for i in range(2, n+1):
            
            fc[i] = fc[i-1] + fc[i-2]
        
        return fc[n]
```

