[toc]

---

### 1. 最小差值Ⅰ

![](https://i.loli.net/2019/11/25/eWRdH4CuQDgaLON.jpg)

### 2. 思路

​	这道题的出题人建议回小学重新学一下语文，这描述实在是看不太懂，看的实例才明白的，意思是数组A的每一个元素都可以且仅可以一次+x的，加完之后得到数组B，求数组B的最小差值。写代码的时候这个思路是我直觉感知到的，现在也没有想好一个完备的逻辑来证明。

### 3. 代码

```python
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        
        if len(A) <= 1:
            return 0
        
        result = max(A) - min(A) - 2*K

        return result if result > 0 else 0
```

