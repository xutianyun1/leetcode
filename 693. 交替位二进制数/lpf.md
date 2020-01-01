```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_str = bin(n)[2:]
        for i in range(1, len(n_str)):
            if n_str[i] == n_str[i-1]:
                return False
        return True
```

### 比较简单

##### 执行用时 :36 ms, 在所有 python3 提交中击败了77.15%的用户
##### 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户

