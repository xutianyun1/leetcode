#### 1. 用两个栈实现队列



用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]


示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]


提示：


	1 <= values <= 10000
	最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 2. 思路

​	想当然的就是，一个栈负责入队，一个栈负责出队，即出队是，就用两个栈之间的数据传输实现倒序，这样就可以按照栈的方式进行FIFO。有一处代码优化的地方就是，并不需要每次出队都进行一次数据传输。仅仅当负责出队的栈为空时，才需要进行数据传输。

#### 3. 代码

```python
class CQueue:

    def __init__(self):
        #    声明两个栈
        self.st1 = []       
        self.st2 = []


    def appendTail(self, value: int) -> None:
        self.st1.append(value)

  
    def deleteHead(self) -> int:
        
        if self.st2:
            return self.st2.pop()
        if not self.st1:
            return -1
        
        while self.st1:
            self.st2.append(self.st1.pop())
            
        return self.st2.pop()
        
    


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

