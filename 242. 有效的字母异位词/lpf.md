给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true
示例 2:

    输入: s = "rat", t = "car"
    输出: false
说明:
你可以假设字符串只包含小写字母。



    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            # return True if sorted(s) == sorted(t) else False

            # return True if sorted(list(s)) == sorted(list(t)) else False
    
            char_dict = {}
            for i in t:
                char_dict[i] = char_dict.get(i, 0) + 1
            
            for j in s:
                char_dict[j] = char_dict.get(j, 0) - 1
    
            if len(char_dict) <= 0:
                return True
    
            if max(char_dict.values()) == 0 and min(char_dict.values()) == 0:
                return True
    
            return False
            

### 一开始用dict的做的，略麻烦但是速度最快利用排序可以一行代码实现，果然人生苦短我用python

##### 执行用时 :60 ms, 在所有 python3 提交中击败了79.00%的用户
##### 内存消耗 :14.1 MB, 在所有 python3 提交中击败了17.88%的用户
