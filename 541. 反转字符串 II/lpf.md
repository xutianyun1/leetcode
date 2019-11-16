给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

    输入: s = "abcdefg", k = 2
    输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


    class Solution:
        def reverseStr(self, s: str, k: int) -> str:
            str_len = len(s)
            if str_len < k:
                return s[::-1]
            elif str_len <= 2*k:
                return s[:k][::-1] + s[k:]
            else:
                n = int(str_len / k)
                min = 0
                max = 1
                s_revers = ''
                for i in range(1, n+1):
                    if i%2 == 1:
                        s_revers += s[min*k:max*k][::-1]
                    else:
                        s_revers += s[max*k:max*k+k]
                        min = max + 1
                        max = max + 2
                if n%2 == 1:
                    return s_revers + s[max*k:]
                else:
                    return s_revers + s[min*k:][::-1]
                    
### 特点：粗暴不简单，逻辑较为复杂

##### 执行用时 :44 ms, 在所有 python3 提交中击败了77.21%的用户
##### 内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.84%的用户
