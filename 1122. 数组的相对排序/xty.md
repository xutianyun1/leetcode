[toc]

---

### 1.  数组的相对排序

![](https://i.loli.net/2019/12/05/Uf61qmnGdsZR9tg.jpg)

### 2. 思路

​	先将在arr1中出现在arr2的元素的个数存储在一个字典中，键是元素，值是该元素的个数。

​	再建一个列表用于存储未出现在arr2中的元素，并将其排序

​	最后根据字典和列表重新生成arr1

### 3. 代码

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #    创建一个字典，用于存储arr1中出现在arr2中相应元素的个数
        arr1_dict = {}
        for n in arr2:
            arr1_dict[n] = arr1.count(n)
        #    arr1中未在arr2中出现的元素
        not_append = []        
        for n in arr1:
            if n not in arr2:
                not_append.append(n)
        #    排序
        not_append.sort()
        
        re = []
        for key in arr1_dict:
            re += [key]*arr1_dict[key]
        
        return re + not_append
```

