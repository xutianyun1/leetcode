#### 1. 剑指offer 10-1. 斐波那契数列

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5


提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 2.代码

# 

1. 创建等长数组，存放之前的斐波那契数列的元素

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        count = [0]*(n+1)
        count[1] = 1
        for i in range(2, n+1):
            count[i] = count[i-1] + count[i-2]
        return count[n] % 1000000007
```



2. 每次计算其实只用到了前两个数，因此，只需要保存前两个数即可。

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f0 = 0
        f1 = 1
        
        for i in range(2, n+1):
            f2 = f0 + f1
            f0, f1 = f1, f2
        return f2 % 1000000007
```

3. 递归

```python
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        
        if n < 2:
            return n
        return (self.fib(n-1) + self.fib(n-2))%1000000007
        
```

