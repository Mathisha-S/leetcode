class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for n in nums:
                if n not in current:
                    current.append(n)
                    backtrack(current)
                    current.pop()

        backtrack([])

        return result