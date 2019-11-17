[toc]

---

#### 1. 字符的最短距离

![](https://i.loli.net/2019/11/17/I8VXGLmsHY9R26j.jpg)

#### 2. 思路

​     初始化一个填充字符串S长度的且长度为字符串长度的列表result。  

​	 扫描字符串S，遇到字符C后，以字符C为中心开始左右遍历，设置变量j表示此时遍历的元素的下标，往左遍	 历的时候，与字符C的距离为 i-j；往右遍历的时候，与字符C的距离为 j-i。当i-j或j-i小于result里的元素时，更	 新result元素。

#### 3. 代码

```python
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        #    结果列表，初始化为最大值即字符串S的长度
        result = [len(S)]*len(S)
        for i in range(len(S)):
            
            #    遇到字符C后，左右分别遍历求最小距离
            if S[i] == C:
                result[i] = 0
                #    左边
                j = i-1
                while j>=0 and S[j] != C:
                    
                    result[j] = (i-j) if result[j] > i-j else result[j]
                    j-=1
                #    右边   
                j = i+1
                while j<len(S) and S[j] != C:
                     
                    result[j] = (j-i) if result[j] > j-i else result[j]
                    j+=1
                    
        return result
```

