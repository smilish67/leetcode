class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        major = 0
        
        for cand in nums:
            if count == 0:
                major = cand
            if major == cand:
                count += 1
            else:
                count -= 1
            
        return major
    