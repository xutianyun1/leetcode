[toc]

---

#### 1. 判断子序列

![](https://i.loli.net/2019/11/17/jtTbvk74Mg1aAx2.jpg)

#### 2. 思路

​	这是Li Pengfei的思路，我写的感觉没有他的好些，就贴下他的。

​	index方法的作用：检查字符n在t中是否出现，从t_index下标开始检查。

#### 3. 代码

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        t_index = 0
        
        for n in s:
            
            try:
                t_index = t.index(n, t_index)
                t_index+=1
            except:
                return False
        return True
```

