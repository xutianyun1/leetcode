思路：典型动态规划，用前面的最大和下一位比较


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if index == 0:
                aft = max_sum = num
            else:
                if num > num+aft:
                    aft = num
                else:
                    aft += num
            
            if aft > max_sum:
                max_sum = aft

        return max_sum
```

##### 执行用时 :40 ms, 在所有 Python3 提交中击败了96.65%的用户
##### 内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.24%的用户
