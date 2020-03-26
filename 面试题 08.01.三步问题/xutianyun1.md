[toc]

---

### 1. 三步问题

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

 示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法


 示例2:

 输入：n = 5
 输出：13


 提示:


n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 2， 思路

动态规划，入门级别的把，fn = fn-1 + fn-2 + fn-3。

运算中间取模算是一个trick，否则会超时。

### 3. 代码

```python
class Solution:
    def waysToStep(self, n: int) -> int:
        
        if n < 3:
            return n
        elif n==3:
            return 4
        dp = [0]*5
        
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[4] = (dp[1] + dp[2] + dp[3])%1000000007
            dp[1] = dp[2]
            dp[2] = dp[3]
            dp[3] = dp[4]
            
        return dp[3]
    
        #if n < 3:
        #    return n
        #elif n == 3:
        #    return 4
        #
        #dp = [0]*(n+1)
        #dp[1] = 1
        #dp[2] = 2
        #dp[3] = 4
        #for i in range(4,n+1):          
        #    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        #
        #return dp[n]%1000000007
        
        
        #if n < 3:
        #    return n
        #if n == 3:
        #    return 4
        #
        #fn = self.waysToStep(n-1)+self.waysToStep(n-2)+self.waysToStep(n-3)
        #
        #return fn
```

