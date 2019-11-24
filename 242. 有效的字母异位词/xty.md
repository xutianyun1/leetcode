[toc]

---

### 1.  有效的字母异位词

![](https://i.loli.net/2019/11/24/q1UeZVctBQr46f2.jpg)

### 2. 思路

​	这道题就比较水了，第一反应就是先转成列表，排序后再转字符串比较。

​    麻烦点 就用各字典存储下字母的数量，然后比较。

### 3. 代码

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #    转成列表
        s_list, t_list= list(s), list(t)
        #    排序
        s_list.sort(),t_list.sort()
        #    再转为字符比较是否相同
        return True if ''.join(s_list) == ''.join(t_list) else False
```

