思路：比较简单，先获取本行的最小值，然后找出index，在跟本列的最小值比较。如果最小值不唯一则会稍微麻烦


```python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_l = []
        for index1, list1 in enumerate(matrix):
            min_num = min(list1)
            min_index = list1.index(min_num)
            if max([list2[min_index] for list2 in matrix]) == min_num:
                min_l.append(min_num)
        return min_l
```


##### 执行用时 :48 ms, 在所有 Python3 提交中击败了82.97%的用户
##### 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

