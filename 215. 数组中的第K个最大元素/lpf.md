
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
```
        

### 本题比较简单，一行

##### 执行用时 :72 ms, 在所有 python3 提交中击败了92.87%的用户
##### 内存消耗 :13.4 MB, 在所有 python3 提交中击败了98.42%的用户
