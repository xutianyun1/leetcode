```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # for index in range(len(s)):
        index = 2
        nums = 0
        while index <= len(s):
            r_nums = s[:index].count('R')
            l_nums = s[:index].count('L')
            if r_nums == l_nums:
                nums += 1
            # else:
            index += 2

        return nums
```

### 思路比较简单，就是循环，然后统计数量，相同就加1

##### 执行用时 :36 ms, 在所有 Python3 提交中击败了79.67%的用户
##### 内存消耗 :12.7 MB, 在所有 Python3 提交中击败了100.00%的用户

