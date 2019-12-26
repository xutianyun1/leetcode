[toc]

---

### 1. 复写零

![](https://i.loli.net/2019/12/26/mz3dPXR6jqJMhun.jpg)

### 2. 思路

so easy。

### 3. 代码

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #    0
        zero = 0
        #    原始arr长度
        N = len(arr)
        #    循环变量
        i = 0
        
        while i < len(arr):
            
            if arr[i] == 0:
                
                arr.insert(i, zero)
                arr.pop()
                i += 2
            else:
                i += 1
        
        
        return None
```

