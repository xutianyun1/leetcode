给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

    输入: "()"
    输出: true
示例 2:

    输入: "()[]{}"
    输出: true
示例 3:

    输入: "(]"
    输出: false
示例 4:

    输入: "([)]"
    输出: false
示例 5:

    输入: "{[]}"
    输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {'{':'}',  '(':')', '[':']'}
        if len(s) % 2 == 1:
            return False
        for i in ['{', '(', '[']:
            if s.count(i) != s.count(brackets_dict[i]):
                return False
        l = ['{', '[', '(']
        l_list = []
        for i in s:
            if i in l:
                l_list.append(i)
            else:
                if len(l_list) == 0:
                    return False
                if not brackets_dict.get(l_list[-1], False):
                    return False
                if i != brackets_dict[l_list[-1]]:
                    return False
                else:
                    l_list.pop()
        return True
        
        
### 代码还可以更简洁，利用栈的特点来解决

##### 执行用时 :44 ms, 在所有 python3 提交中击败了75.17%的用户
##### 内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.51%的用户