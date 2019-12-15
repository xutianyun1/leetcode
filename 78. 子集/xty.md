[toc]

---

### 1. 子集

![](https://i.loli.net/2019/12/15/Iu1sEtVr35jiv7l.jpg)

### 2. 思路

假设输入数组的长度为3，那么000，001，010，---，111，将为1的下标的nums的元素组成子集。

### 3. 代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        #    数组的位数，也是后面二进制的位数
        n = len(nums)
        #    转为二进制
        bin_n = '0b' + '1'*n
        
        i = 0
        re = []
        while i <= int(bin_n,2):
            '''
            每次循环i+1，然后转为二进制，将二进制为1的下标对应于nums的元素加入到temp作为一个子集
            '''
            temp = []
            mat = '{:0' + str(n) + 'b}'
            #    转为二进制并高位补0
            k = mat.format(i).replace('0b','')
            #    检测二进制哪一位为1，
            for j in range(len(k)):
                if k[j] == '1':
                    #    将为1的位，将nums中对应的元素加入到temp中
                    temp.append(nums[j])
            re.append(temp)
            i += 1
        return re
```

