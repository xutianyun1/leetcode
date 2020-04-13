[toc]

---

### 1. 用栈实现队列

使用栈实现队列的下列操作：


	push(x) -- 将一个元素放入队列的尾部。
	pop() -- 从队列首部移除元素。
	peek() -- 返回队列首部的元素。
	empty() -- 返回队列是否为空。


示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:


	你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
	你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
	假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 2. 思路

就常规操作，可能就删除不好弄把，要先把栈中的元素全部取出，然后删栈底元素，最后再将全部元素都入栈。

### 3. 代码

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.st_index = -1
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st_index += 1
        if len(self.stack) == self.st_index:
            self.stack.append(x)
        else:
            self.stack[self.st_index] = x
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.temp = []
        while self.st_index > -1:
            self.temp.append(self.stack[self.st_index])
            self.st_index -= 1
        
        re = self.temp.pop()
        self.temp = self.temp[::-1]
        for n in self.temp:
            self.st_index += 1
            self.stack[self.st_index] = n
        return re
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.st_index == -1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```



