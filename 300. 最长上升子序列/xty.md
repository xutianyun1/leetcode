[toc]

---

### 1. 最长上升子序列

![](https://i.loli.net/2019/12/19/axAXkO6iqjIeUKL.jpg)

### 2. 思路

我能想到的就是暴力，O(n**2)的时间复杂度。

### 3. 代码

```python

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = 0
        
        for i in range(len(nums)):
            length_i = 1
            a = nums[i]
            for j in range(i, len(nums)):
                
                if nums[j] > a:
                    if j < len(nums)-1 and nums[j+1] < nums[j] and nums[j+1] > a:
                        continue
                    length_i += 1
                    a = nums[j]
            if length_i > length:
                length = length_i
                
        return length
                    
                
```

### 4. 评论里大神出没

https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/



![](https://i.loli.net/2019/12/19/qZCT5FyVOxGMwK9.jpg)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```

