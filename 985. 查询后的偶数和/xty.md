[toc]

---

### 1. 查询后的偶数和

![](https://i.loli.net/2019/12/25/iy3XL4fG2YjzEhM.jpg)

### 2. 思路

挺简单的。先计算原有的偶数和even_sum，然后查询后分四种情况，对even_sum进行更新

### 3. 代码

```python
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        N = len(queries)
        re = [0]*(N+1)
        
        
        even_sum = 0
        for j in range(len(A)):     
            if A[j]%2 == 0:
                even_sum += A[j]
        re[0] = even_sum
        for i in range(N):
            before = A[queries[i][1]]
            after = A[queries[i][1]] + queries[i][0]
            if before%2 == 0 and after%2 == 0:
                re[i+1] = re[i] + queries[i][0]
            elif before%2 == 0 and after%2 != 0:
                re[i+1] = re[i] - before
            elif before%2 != 0 and after%2 == 0:
                re[i+1] = re[i] + after
                print(re[i+1])
            else:
                re[i+1] = re[i]
                
            A[queries[i][1]] = after
        
        return re[1:]
```

### 4. 官方题解



```python
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        N = len(queries)
        re = [0]*N
        
        
        even_sum = 0
        for j in range(len(A)):     
            if A[j]%2 == 0:
                even_sum += A[j]
        even_sum
        for i in range(N):
            before = A[queries[i][1]]
            after = A[queries[i][1]] + queries[i][0]
            if before%2 == 0:
                even_sum -= before
            if after%2 == 0:
                even_sum += after
            
            re[i] = even_sum
                
            A[queries[i][1]] = after
        
        return re
```



将情况进行了简化，如果未更新前的A数组的值是偶数，则将偶数和even_sum减去该偶数值，然后检测更新后的A数组的值是否为偶数，如果为偶数则将even_sum加上该偶数值。