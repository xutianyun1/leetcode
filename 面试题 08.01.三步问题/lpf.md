三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

     输入：n = 3 
     输出：4
     说明: 有四种走法
示例2:

     输入：n = 5
     输出：13
提示:

    n范围在[1, 1000000]之间

```python
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            num = 0
            last1 = 4
            last2 = 2
            last3 = 1
            for i in range(4, n+1):
                num = (last1 + last2 + last3) % 1000000007
                last3 = last2
                last2 = last1
                last1 = num
        
        return num
```

## 思路：典型动态规划

##### 执行用时 :288 ms, 在所有 Python3 提交中击败了97.51%的用户
##### 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

