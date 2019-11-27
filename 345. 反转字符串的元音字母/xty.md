[toc]

---

### 1. 反转字符串中的元音字母

![](https://i.loli.net/2019/11/27/hVSPa62oFiIwnQ5.jpg)

### 2. 思路

​		**双指针法**

​		

### 3. 代码

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        #    a、e、i、o、u
        i, j = 0, len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        while i < j:
            
            while i < len(s) and s_list[i] not in vowels:   
                i+=1
            while j >= 0 and s_list[j] not in vowels:   
                j-=1
            
            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i+=1
                j-=1
            
        return ''.join(s_list)
                
```

