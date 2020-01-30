[toc]

---

### 1. 小镇的法官

![](https://raw.githubusercontent.com/xutianyun1/cloudimage/master/img/997.png)



### 2. 思路

法官不相信任何人，所以他不会出现在第一个元素的位置上，每一个人都信任法官，因此，法官的应该出现在的第二个元素的位置应该是N-1。建立两个一维数组（长度为N+1），每个数组的下标代表一个是市民（0除外），用以记录，该市民出现在第一个元素位置和第二个元素位置的次数。

### 3.代码

```python

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N==1:
            return N
        
        de1 = [0]*(N+1)
        de2 = [0]*(N+1)
        
        for n in trust:
            de1[n[0]] += 1
            de2[n[1]] += 1
        k = -1
        for i,j in zip(de1,de2):
            k += 1
            if i==0 and j==N-1:
                return k
        return -1
    

```

