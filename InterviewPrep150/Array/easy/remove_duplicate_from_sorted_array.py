def removeDuplicate(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if i == len(nums)-1:
            break
        if nums[i] == nums[i+1]:
            del nums[i+1]
            i -= 1
        i+=1
    return nums