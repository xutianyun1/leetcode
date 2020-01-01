TODO 超时，有空做
```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        friends = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i != j:
                    j_age = ages[j]
                    if j_age < 15:
                        continue
                    i_age = ages[i]
                    if not ((j_age <= 0.5 * i_age + 7) or (j_age > i_age)):
                        friends += 1

        return friends
```