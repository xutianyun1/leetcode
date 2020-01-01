```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in range(len(nums)):
            for subset in subsets[:]:
                subsets.append(subset+[nums[i]])
        return subsets
```

### 求所有的子集，循环所有的值，以往所有的结果都加入就是所有子集

##### 执行用时 :32 ms, 在所有 python3 提交中击败了98.56%的用户
##### 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.86%的用户
