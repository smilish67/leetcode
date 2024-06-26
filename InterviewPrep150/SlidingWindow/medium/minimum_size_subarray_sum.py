class Solution:
    #time limit exceeded solution. it's because it tooks O(n^2)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_cnt = len(nums)+1


        for left in range(len(nums)):
            sums  = 0
            cnt = 0
            right = left
            while right < len(nums):
                sums += nums[right]
                cnt += 1
                if sums >= target:
                    if min_cnt > cnt:
                        min_cnt = cnt
                        break
                right += 1

        if min_cnt <= len(nums):
            return min_cnt
        else:
            return 0