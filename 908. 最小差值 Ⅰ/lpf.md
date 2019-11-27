	class Solution:
		def smallestRangeI(self, A: List[int], K: int) -> int:
			max_ = max(A)
			min_ = min(A)
			if max_ - min_ <= 2*K:
				return 0
			else:
				return max_-K - (min_ + K)


### 本题较为简单，没啥可说的，想明白了就是几行代码的事		
				
##### 执行用时 :176 ms, 在所有 python3 提交中击败了42.29%的用户
##### 内存消耗 :14.9 MB, 在所有 python3 提交中击败了6.00%的用户

