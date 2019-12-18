[toc]

---

### 1. 全排列

![](https://i.loli.net/2019/12/18/Yvqo5PiUpAhxZwe.jpg)

### 2. 思路

递归、分治



### 3. 代码

```python
class Solution:
    
    _re = []
    def func(self, pre, nums):
        '''
        pre: 已选定的元素列表
        nums: 剩余待选的元素列表
        re: 结果列表
        '''
        if len(nums) == 0:
            print(pre)
            self._re.append(pre)
            return
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            self.func(pre + [nums[i]], temp)
                                                                                                 
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        #    每次执行该方法都初始化空列表
        self._re = []
        pre = []            
        #    递归
        self.func(pre, nums)           
        return self._re
        
```

