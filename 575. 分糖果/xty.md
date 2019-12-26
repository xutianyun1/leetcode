[toc]

---

### 1. 分糖果

![](https://i.loli.net/2019/12/26/vdUOu82eYs4IkWC.jpg)

### 2.  思路

都在代码的注释里 了

### 3. 代码

```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        #    对candies进行去重处理
        #    candies_set表示的便是糖果的种类
        candies_set = set(candies)
        #    如果糖果的种类数大于一半的糖果数量
        #    因为需要平均分糖果，因此妹妹此时最多能或的糖果种类数便是糖果数量的一半
        if len(candies_set) > len(candies) >> 1:
            return len(candies) >> 1
        #    否则，妹妹最多可以获的糖果种类数，便是len(candies_set)
        else:
            return len(candies_set)
        

```

