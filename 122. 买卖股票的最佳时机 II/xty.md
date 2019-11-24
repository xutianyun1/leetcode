[toc]

---

### 1. 股票买卖的最佳时机

![](https://i.loli.net/2019/11/22/WKnkygspBivxM1F.jpg)

### 2. 思路

​			做的时候理解错题意了，认为一天只能完成一笔交易。唉，难受，

​			扫描列表，维护一个局部最小值，发现局部最小值后，买入，继续往后扫描，直到发现下一个元素小于上一个元素的时候 表明可能会出现下一个局部最小值，此时卖出股票, 若扫描到最后仍然没有发现有出现下个局部最小值的趋势，此时在列表的最后一天卖出股票。循环往复，直至列表扫描完成。

### 3. 代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        index = 0
        
        while index < len(prices)-1:
            
            if min_price >= prices[index]:
                min_price = prices[index]
                
                while prices[index] < prices[index+1]:
                    
                    index += 1
                    if index == len(prices)-1:
                        return max_profit + prices[index] - min_price
                    
                max_profit += prices[index] - min_price
                min_price = prices[index]
                
            index += 1
        return max_profit
```

```
执行用时 :72 ms, 在所有 python3 提交中击败了97.20%的用户
内存消耗 :14.7 MB, 在所有 python3 提交中击败了5.31%的用户
```

