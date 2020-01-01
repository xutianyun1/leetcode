```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        classes = len(set(candies))
        len_2 = int(len(candies)/2)
        return classes if classes <= len_2 else len_2
```

### 很简单，不在赘述

##### 执行用时 :1072 ms, 在所有 python3 提交中击败了59.34%的用户
##### 内存消耗 :14.6 MB, 在所有 python3 提交中击败了82.84%的用户

