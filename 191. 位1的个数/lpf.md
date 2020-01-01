```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
```


### 本题比较简单，一句话出来

##### 执行用时 :24 ms, 在所有 python3 提交中击败了99.32%的用户
##### 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户


