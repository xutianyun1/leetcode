给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:

    s = "abc", t = "ahbgdc"
    返回 true.

示例 2:

    s = "axc", t = "ahbgdc"
    返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


    class Solution:
        def isSubsequence(self, s: str, t: str) -> bool:
            index_place = 0
            for i in s:
                try:
                    index_place = t.index(i, index_place)
                    index_place+=1
                except:
                    return False
            return True

### 特点：清晰明了

##### 执行用时 :44 ms, 在所有 python3 提交中击败了96.63%的用户
##### 内存消耗 :18.5 MB, 在所有 python3 提交中击败了5.26%的用户

