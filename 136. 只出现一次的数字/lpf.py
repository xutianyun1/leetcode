class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        only_list = []
        for s in nums:
            if s not in only_list:
                only_list.append(s)
            else:
                only_list.remove(s)

        return only_list[0]




# 简单粗暴

# 执行用时 :1468 ms, 在所有 python3 提交中击败了8.77%的用户
# 内存消耗 :16.2 MB, 在所有 python3 提交中击败了5.03%的用户