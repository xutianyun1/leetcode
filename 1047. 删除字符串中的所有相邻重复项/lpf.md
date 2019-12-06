    class Solution:
        def removeDuplicates(self, S: str) -> str:
            # stack = []
            # for char in S:
            #     if stack and stack[-1] == char:
            #         stack.pop()
            #     else:
            #         stack.append(char)
            # return ''.join(stack)
    
    
            S = list(S)
            index = 1
            while index < len(S):
                if S[index] == S[index-1]:
                    del S[index], S[index-1]
                    if index > 1:
                        index = index - 1
                else:
                    index+=1
            return ''.join(S)
            
            

### 我想到的解决方法是list一下字符串，然后利用pytohn对list的操作解题
### 注释是看大佬们的解决方法，速度比我的垃圾方法快的多

##### 124 ms, 在所有 python3 提交中击败了22.66%的用户
##### 内存消耗 :12.8 MB, 在所有 python3 提交中击败了100.00%的用户


大佬的：
执行用时 :64 ms, 在所有 python3 提交中击败了98.30%的用户
内存消耗 :12.9 MB, 在所有 python3 提交中击败了100.00%的用户
