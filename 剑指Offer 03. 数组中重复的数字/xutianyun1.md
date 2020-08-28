#### 1.找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 


限制：

2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 2. 思路

建立一个等长的数组num_count，初始化为0，

遍历nums，将nums中元素作为num_count的下标，对num_count中的元素进行加一。

遍历结束后，num_count中的元素值就是对应下标在nums中出现的次数。

最后遍历num_count,将第一个元素值大于1的下标作为返回结果

时间O(n)、空间O(n)

#### 3. 代码

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        num_count = [0]*len(nums)
        for n in nums:
            num_count[n] += 1
        print(num_count)
        for index in range(len(num_count)):
            if num_count[index] > 1:
                return index
```

#### 4. 改进

在原思路的基础上进行改进，第一次遍历时便检测num_count中的元素值是否大于1，若大于1直接返回

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        num_count = [0]*len(nums)
        for n in nums:
            num_count[n] += 1
            if num_count[n] > 1:
                return n

```

