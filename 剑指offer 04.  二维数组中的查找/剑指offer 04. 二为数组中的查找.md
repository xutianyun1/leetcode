#### 1. 二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 2. 思路

以右上角的角度观察，是一个二分查找树。即如果target小于n，则往左走，如果traget大于n，则往下走。

#### 3. 代码

```python
class Solution:


    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        index = [0, len(matrix[0])-1]

        while index[0] < len(matrix) and index[1] >= 0:
            print(matrix[index[0]][index[1]])
            if matrix[index[0]][index[1]] == target:
                return True
            if matrix[index[0]][index[1]] > target:
                index[1] -= 1
            else:
                index[0] += 1
        return False
```



