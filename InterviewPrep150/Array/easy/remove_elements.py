class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

rmv = Solution()
ak = rmv.removeElement([1,2,3,4,3,3,4,3,1,1,2,3], 3)
print(ak)