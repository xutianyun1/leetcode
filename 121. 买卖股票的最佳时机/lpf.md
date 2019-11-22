给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

**示例 1**:

```
输入: [7,1,5,3,6,4]
输出: 5
```

解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

**示例 2**:

```
输入: [7,6,4,3,1]
输出: 0
```


    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            diff = 0
            min_ = 0
            for i in range(0, len(prices)):
                if i > 0:
                    if prices[i] - min_ > diff:
                        diff = prices[i] - min_
                    else:
                        if prices[i] < min_:
                            min_ = prices[i]
                else:
                    min_ = prices[i]

        return diff if diff >= 0 else 0
        
        
### 本题比较简单，动态更新diff和最小值，然后进行对比

##### 执行用时 :80 ms, 在所有 python3 提交中击败了88.70%的用户
##### 内存消耗 :14.8 MB, 在所有 python3 提交中击败了5.32%的用户