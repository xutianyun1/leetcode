[toc]

---

#### 1. 第一个错误的版本

![](https://i.loli.net/2019/11/17/uBtVsZSH1T2RWPw.jpg)

#### 2. 思路

​		**二分查找**

​		判断条件：mid是错误版本，但mid-1是正确版本。



#### 3. 代码

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        low, high = 1, n
        mid = (low+high)>>1
        while low <= high:
            if isBadVersion(mid):
                if (mid-1 >= 1 and not isBadVersion(mid-1)) or mid == 1 :
                    return mid
                high = mid
            else:
                low = mid+1
            mid = (low+high)>>1
```

