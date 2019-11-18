假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**注意**：给定 n 是一个正整数。

**示例 1**：

```
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。

1.  1 阶 + 1 阶
2.  2 阶
```

**示例 2**：

```
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。

1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


    
    
    class Solution:
        def climbStairs(self, n: int) -> int:

        fc = [0]*(n+1)
        fc[0] = 1
        fc[1] = 1
        for i in range(2, n+1):
            fc[i] = fc[i-1] + fc[i-2]
        
        return fc[n]

        # def get(n):
        #     if n == 2:
        #         return 2
        #     if n == 1:
        #         return 1
        #     return get(n-1) + get(n-2)

        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return get(n)
        
### 想了半天，类似斐波那契数列，但用常用的递归却超时了，还是运哥的方法牛皮一点

