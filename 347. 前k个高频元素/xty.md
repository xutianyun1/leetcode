[toc]

---

### 1. 前k个高频元素

![](https://i.loli.net/2019/12/21/2xBtQY9eURy4hCb.jpg)

### 2. 思路

先用一个字典存储元素出现的频数，key=元素值，value=该元素值出现的频数

根据字典的value排序，只取前k个即可

### 3. 代码

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}
        fre_k = []
        for n in nums:    
            if n not in nums_dict:         
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1
            
        
        for key in sorted(nums_dict, key=nums_dict.__getitem__, reverse=True):
            fre_k.append(key)  
        return fre_k[:k]
```

