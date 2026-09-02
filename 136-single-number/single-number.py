class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =0
        for n in nums:
            result^=n
        return result
# ^ cancels the same numbers 
#   n  res    op    res
# 1	4	0	0 ^ 4	4
# 2	1	4	4 ^ 1	5
# 3	2	5	5 ^ 2	7
# 4	1	7	7 ^ 1	6
# 5	2	6	6 ^ 2	4