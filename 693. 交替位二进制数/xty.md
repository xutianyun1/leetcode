[toc]

---

### 1. 交替位二进制数

![](https://i.loli.net/2019/12/09/aJywKnvufsDc516.jpg)



###  2. 思路

​		比较直观的就是将字符该整数转为二进制，然后检查字符'11'和字符’00‘  是否在该二进制中

### 3. 代码

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        #    转换为二进制
        n_bin = bin(n).replace('0b', '')
        
        if n_bin.find('11') == -1 and n_bin.find('00') == -1:
            return True
        return False
        
```



