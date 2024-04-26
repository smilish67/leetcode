def removeDuplicate(nums: list[int]) -> int:
    i = 0
    buffer = 0
    while i < len(nums):
        if i == len(nums) -1:
            break
        if nums[i] == nums[i+1]:
            if buffer < 1:
                buffer += 1
            else:
                del nums[i+1]
                i -=1
        else:
            buffer = 0
        i += 1
    return len(nums)