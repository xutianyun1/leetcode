[toc]

---

### 1. 适龄的朋友

![](https://i.loli.net/2019/12/25/kRJaBv6ZGrObM1N.jpg)

### 2. 思路

不知道那个狗东西给添加的示例，那么长，能不超出时间限制嘛。

只能通过字典来去重减少数组的长度，再计算。

具体的，对原数组去重处理，然后创建一个字典用于每个年龄在原数组中出现的次数，对去重的后数组嵌套两次遍历，同时需要注意的是，需要检测同龄的人是否可以发送好友请求，如果可以，

### 3. 代码

```python
class Solution:
    
    def is_send(self, A, B):
        '''
        检测A是否可以给B发送好友请求
        '''
        if (B <= (0.5 * A + 7)) or (B > A) or (B > 100 and A < 100):
            return False
        return True
    
    def numFriendRequests(self, ages: List[int]) -> int:
        
        re = 0
        #    去重
        ages1 = list(set(ages))
        #    key：ages1中的元素。value：key在ages中出现的次数
        ages1_nums = {}
        for n in ages1:
            ages1_nums[n] = ages.count(n)
        #    对去重后的数组进行遍历
        for i in range(len(ages1)):
            #    检测是否可以给同龄的人发送好友请求
            if self.is_send(ages1[i], ages1[i]):
                re += (ages1_nums[ages1[i]]-1)*ages1_nums[ages1[i]]
            #    遍历
            for j in range(len(ages1)):
                if i!=j and self.is_send(ages1[i], ages1[j]):
                    re += ((ages1_nums[ages1[i]])*(ages1_nums[ages1[j]]))
        return re
                    
```

