```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        last = 0 
        now = 0
        for i in nums: 
            # 这是一个动态规划问题
            # 动态规划。最大利益 = max（上家的最大利益，上家的上家的最大利益 + 当前家的利益）
            last, now = now, max(last + i, now)
        return now
```

### 大佬的思路，很牛皮


