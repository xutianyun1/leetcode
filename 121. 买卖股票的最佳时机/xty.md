[toc]

---

### 1. 买卖股票的最佳时机

![](https://i.loli.net/2019/11/21/FlWUiyMXg5GIapj.jpg)

### 2. 思路

​		对给出的列表进行扫描，维护一个最低股票价格和能够获取的最大利润。

### 3. 代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = min_price - prices[0]
        
        for n in prices:
            
            if n < min_price:
                min_price = n
            if n - min_price > max_profit:
                max_profit = n - min_price
            
        return max_profit
```



