    class Solution:
        def reverseVowels(self, s: str) -> str:
            s_copy = list(s)
            yuan = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            s_index = []
            for index, char in enumerate(s):
                if char in yuan:
                    s_index.append(index)
    
            for i in range(int(len(s_index)/2)):
                s_copy[s_index[i]] = s[s_index[-(i + 1)]]
                s_copy[s_index[-(i + 1)]] = s[s_index[i]]
    
            return ''.join(s_copy)
            

### 方法比较蠢，速度也很慢，但好歹也算实现了

##### 执行用时 :100 ms, 在所有 python3 提交中击败了25.60%的用户
##### 内存消耗 :16.2 MB, 在所有 python3 提交中击败了5.49%的用户
