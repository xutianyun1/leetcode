**_思路：按照小学加法的规则硬写，太难了，看着我的代码都头疼**_

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) >= len(num2):
            max_num = num1
            min_num = num2
        else:
            max_num = num2
            min_num = num1
        min_len = len(min_num)
        max_len = len(max_num)
        add = 0
        result = ''
        if min_len != max_len:
            balance = max_len - min_len
        else:
            balance = 0
        for index in range(min_len - 1, -1, -1):
            if int(max_num[index + balance]) + int(min_num[index]) + add >= 10:
                result = str(int(max_num[index + balance]) + int(min_num[index]) + add)[-1] + result
                add = 1
            else:
                result = str(int(max_num[index + balance]) + int(min_num[index]) + add)[-1] + result
                add = 0

        for index in range(max_len-min_len-1,  -1, -1):
            if int(max_num[index]) + add >= 10:
                result = str(int(max_num[index]) + add)[-1] + result
                add = 1
            else:
                result = str(int(max_num[index]) + add)[-1] + result
                add = 0
        if add:
            head = result[0]
            result = str(add) + result
        return result
```

##### 执行用时 :88 ms, 在所有 Python3 提交中击败了17.48%的用户
##### 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.34%的用户


