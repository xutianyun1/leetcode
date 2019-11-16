给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            only_list = []
            for s in nums:
                if s not in only_list:
                    only_list.append(s)
                else:
                    only_list.remove(s)
            return only_list[0]




### 特点：简单粗暴。缺点：耗时太太太太长。

##### 执行用时 :1468 ms, 在所有 python3 提交中击败了8.77%的用户
##### 内存消耗 :16.2 MB, 在所有 python3 提交中击败了5.03%的用户