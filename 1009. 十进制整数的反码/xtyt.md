[toc]

---

### 1. 十进制数的反码

![](https://i.loli.net/2019/12/28/6zdbpCRmilQtOwZ.jpg)

### 2. 思路

so easy。先将十进制数转为二进制字符串，然后遍历该字符串，将字符串值与1异或，再分别加入到Inv_code中。最后再转为十进制

### 3. 代码

```python
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        N_bin = bin(N)
        
        Inv_code = '0b'
        
        for i in range(2, len(N_bin)):
            Inv_code += str(int(N_bin[i]) ^ 1)

        return int(Inv_code, 2)
```

