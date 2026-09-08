class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maximum = window

        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i - k]
            maximum = max(maximum, window)

        return maximum / k