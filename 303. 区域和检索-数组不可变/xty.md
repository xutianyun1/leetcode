[toc]

---

### 1. 区域和检索-数组不可变

![](https://i.loli.net/2019/12/17/jup3cl8bswxO2TL.jpg)

### 2. 思路

so easy

###  3.  代码

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

