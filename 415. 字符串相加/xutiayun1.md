[toc]

----

### 1. 字符串相加



给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：


	num1 和num2 的长度都小于 5100.
	num1 和num2 都只包含数字 0-9.
	num1 和num2 都不包含任何前导零。
	你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

### 2. 思路

把两个字符串倒序为列表，然后对两个列表元素逐个相加，值得注意的是需要对进位不同情况处理。

### 3. 代码

```python
class Solution:
     
    def func(self,i,re):
        '''
        对进位进行处理
        '''
        if i > 9:
            re += str(i-10)
            i = 1
        else:
            re += str(i)
            i = 0
        return i, re
        
    def addStrings(self, num1: str, num2: str) -> str:
        
        re = ''
        #    转为倒序的列表
        num1_list, num2_list = list(num1)[::-1], list(num2)[::-1]
        #    对于短的进行补零
        if len(num1_list)>len(num2_list):
            num2_list += [0]*(len(num1_list)-len(num2_list))
        else:
            num1_list += [0]*(len(num2_list)-len(num1_list))
            
        i = 0      
        while len(num1_list) and len(num2_list):
            
            i = int(num1_list[0]) + int(num2_list[0]) + i
            i, re = self.func(i, re)
            num1_list.pop(0)
            num2_list.pop(0)
        #   最后判断是否还有进位
        if i>0:
            re += str(i)
        return re[::-1]
            


```



