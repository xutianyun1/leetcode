[toc]

---

### 1. 图像渲染

### 2. 思路

将第一个坐标入队，循环一下过程直至队列为空：将队头元素出队，检查四周是否有和他相等的值，如果有则将其入队，最后将该坐标的值进行渲染，并标记为已渲染。

### 3. 代码

```python
from queue import Queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #    创建队列
        q = Queue()
        #    将第一个坐标入队
        q.put([sr, sc])
        #    标记已经渲染
        drawed = []
        row, c = len(image), len(image[0])
        oriColor = image[sr][sc]
        while not q.empty():
            #    出队
            r = q.get() 
            
            if r[0] > 0 and [r[0]-1, r[1]] not in drawed and image[r[0]-1][r[1]] == oriColor:
                q.put([r[0]-1, r[1]])
            if r[1] > 0 and [r[0], r[1]-1] not in drawed and image[r[0]][r[1]-1] == oriColor:
                q.put([r[0], r[1]-1])
            if r[0] <  row-1 and [r[0]+1, r[1]] not in drawed and image[r[0]+1][r[1]] == oriColor:
                q.put([r[0]+1, r[1]])
            if r[1] < c-1 and [r[0], r[1]+1] not in drawed and image[r[0]][r[1]+1] == oriColor:
                q.put([r[0], r[1]+1])
            
            image[r[0]][r[1]] = newColor
            drawed.append(r)
        return image
                
        
```

