```python
import copy
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        N = copy.deepcopy(M)
        def get_ele(i, j):
            if i<0 or j<0:
                return 0, False
            try:
                return N[i][j], True
            except:
                return 0, False
        for i in range(len(M)):
            for j in range(len(M[0])):
                times = 0
                sum_ele = 0
                for m, n in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1), (i, j)):
                    nums, has_nums = get_ele(m, n)
                    if has_nums:
                        times += 1
                        sum_ele += nums
                M[i][j] = int(sum_ele/times)

        return M
```

### 经典问题

##### 执行用时 :876 ms, 在所有 python3 提交中击败了34.98%的用户
##### 内存消耗 :12.6 MB, 在所有 python3 提交中击败了98.25%的用户



