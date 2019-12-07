[toc]

---

### 1. 员工的重要性

![](https://i.loli.net/2019/12/07/VBUT48xvMmd1uZE.jpg)

### 2. 思路

​	用队列存储下属，用字典key=id。value=emplyees[i].

​	先遍历一遍employees，将其存入，并检测id所指的那个元素，将其直系下属存入low，重要性赋值给importance。再遍历队列，如果其下属还有下属，则将下属的下属也存入low，当队列为空时结束。

### 3. 代码

```python

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #    队列
        low = []
        #    队列首原元素下标，每次访问完首元素后 则+1
        low_index = 0
        importance = 0
        #    key: id value: employees[i]
        employees_dict = {}
        for i in range(len(employees)):
            '''
            创建字典，并检测到id所在元素，将其直系下属存入low中
            '''
            employees_dict[employees[i].id] = employees[i]
            if employees[i].id == id:
                low = employees[i].subordinates
                importance = employees[i].importance

        while low_index < len(low):
            '''
            遍历队列
            '''
            #    将下属的下属也加入到low中
            low += employees_dict[low[low_index]].subordinates
            importance += employees_dict[low[low_index]].importance
            low_index += 1
    
                          
        return importance
```

