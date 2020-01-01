```python
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum_re = sum([num for num in A if num%2 == 0])
        for i in range(len(A)):
            val = queries[i][0]
            index = queries[i][1]
            A[index] += val
            index_val = A[index]
            if index_val%2 == 0 and val%2 == 0:
                sum_re = sum_re + val
                result.append(sum_re)
            elif index_val%2 == 0 and val%2 !=0:
                sum_re = sum_re + index_val
                result.append(sum_re)
            elif index_val%2 != 0 and val%2 ==0:
                result.append(sum_re)
            elif index_val%2 != 0 and val%2 !=0:
                sum_re = sum_re - index_val + val
                result.append(sum_re)
        return result
```

### 简单直接的方法

##### 执行用时 :612 ms, 在所有 python3 提交中击败了89.61%的用户
##### 内存消耗 :18.6 MB, 在所有 python3 提交中击败了5.18%的用户

