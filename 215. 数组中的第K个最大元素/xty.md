[toc]

---

### 1. 数组中的第K个最大元素

![](https://i.loli.net/2019/12/17/a6UvP4OZHGpVyXi.jpg)

### 2. 思路

so easy

### 3. 代码

```python

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        return sorted(nums)[-k]
```

