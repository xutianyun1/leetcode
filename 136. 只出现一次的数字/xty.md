[toc]

------



##### 1. 只出现一次的数字

![](https://i.loli.net/2019/11/16/Y1M7caHbBS2GRsl.jpg)

##### 2. 思路

​	我们对该数组排序后，单独只出现了一次的元素A然在奇数位上出现。  

​    只遍历奇数位数组元素，检测它和后一位元素是否相同，如果不同则返回该元素即可。  

​    Note: 需要注意边缘条件，如果元素A出现在排序后的数组的最后一位，则应该直接返回数组的最后一位。

##### 3. 代码



```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    #    排序
    nums.sort()
    #    只检测奇数位
    for i in range(0,len(nums),2):
        
        if i == len(nums)-1 or nums[i] != nums[i+1]:
            return nums[i]
```
- **执行用时 :116 ms, 在所有 python3 提交中击败了71.14% 的用户**
- **内存消耗 :16.3 MB, 在所有 python3 提交中击败了5.03%的用户**

##### 4. 评论里的思路

**异或**：

> 1. 交换律： a ^ b ^ c == a ^ c ^ b
> 2. 任何数于0异或位任何数: 0^n == n
> 3. 相同的数异或为0: n^n == 0


        

```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for num in nums:
        a = a^num
    return a
```
