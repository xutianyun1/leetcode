```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i: j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```


### 很蠢的方法，出来就好，成绩很差

##### 执行用时 :1192 ms, 在所有 python3 提交中击败了14.16%的用户
##### 内存消耗 :16.1 MB, 在所有 python3 提交中击败了99.71%的用户

