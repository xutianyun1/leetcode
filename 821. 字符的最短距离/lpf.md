给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

    输入: S = "loveleetcode", C = 'e'
    输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


    class Solution:
        def shortestToChar(self, S: str, C: str) -> List[int]:
            l_s = len(S)
            result = [l_s]*l_s
            for index in range(len(S)):
                if S[index] == C:
                    result[index] = 0
                    left = index - 1
                    right = index + 1
                    while result[left] > index-left:
                        result[left] = index-left
                        left -= 1
                    while (right < l_s) and (result[right] != C):
                        result[right] = right - index
                        right += 1
            return result
            
### 特点：思路清晰，比较满意。

##### 执行用时 :60 ms, 在所有 python3 提交中击败了78.82%的用户
##### 内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.40%的用户