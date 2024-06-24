class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # firstly we make problems in a controllable manner removing complete rotation.
        k = k % len(nums)
        
        # M1. append and delete first n-k elements - SLOW
        for i in range(len(nums)-k):
            nums.append(nums[0])
            del nums[0]
        
        # M2. Reverse method
