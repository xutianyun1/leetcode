[toc]

---

### 1. IP地址无效化

![1578927128340](C:\Users\xutia\AppData\Roaming\Typora\typora-user-images\1578927128340.png)

### 2. 思路

python6就完事了

### 3. 代码

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        return address.replace('.','[.]')
```

