    class Solution:
        def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
            result = []
            for char in arr2:
                result = result + [char]*arr1.count(char)
                arr1 = [i for i in arr1 if i != char]
            
            result += sorted(arr1)
            return result
            

### 这题比较简单，主要是python内置函数的使用大大降低了难度

##### 执行用时 :64 ms, 在所有 python3 提交中击败了39.49%的用户
##### 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户

略微优化：
    class Solution:
        def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
            result = []
            for char in arr2:
                result = result + [char]*arr1.count(char)
                
            arr1 = [i for i in arr1 if i not in result]
            result += sorted(arr1)
            return result
            

##### 执行用时 :44 ms, 在所有 python3 提交中击败了95.16%的用户
##### 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户
