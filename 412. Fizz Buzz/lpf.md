```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1, n+1):
            if num % 15 == 0:
                res.append('FizzBuzz')
            elif num % 3 == 0:
                res.append('Fizz')
            elif num % 5 == 0:
                res.append('Buzz')
            else:
                res.append('%s' % num)

        return res
```

### 思路很简单，直接判读

##### 执行用时 :44 ms, 在所有 python3 提交中击败了92.18%的用户
##### 内存消耗 13.8 MB, 在所有 python3 提交中击败了99.38%的用户
