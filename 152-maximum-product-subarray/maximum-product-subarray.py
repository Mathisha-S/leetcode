class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        maximum = nums[0]

        for n in nums[1:]:
            oldMax = currentMax

            currentMax = max(n, n * currentMax, n * currentMin)
            currentMin = min(n, n * oldMax, n * currentMin)

            maximum = max(maximum, currentMax)

        return maximum