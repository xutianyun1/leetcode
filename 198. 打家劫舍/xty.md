[toc]

---

### 1. 打家劫舍

![](https://i.loli.net/2019/12/08/39X8BgCGvhdUOmz.jpg)

### 2. 思路

​		典型的动态规划，偷到第i家的时候，要考虑**第i-1家**是否被偷，有两种情况：**第i-1家**如果被偷，则**第i家**不能偷，此时偷盗金额即使最大金额；如果没被偷 ，则最大金额是**第i-2家**时的金额加上**第i家**的金额。两种情况求个最大值就是偷到**第i家**的最大金额。

### 3. 代码

```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
        i = 2
        while i < len(nums):
            
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            i+=1
            
        return dp[-1]
```



