import random
import time

# Quick sort algorithm with a recursive method.
def quickSort(nums: list[int], left:int, right:int):
        if left == right:
            return nums
        
        pivot = left
        i = left+1
        j = right

        while i <= j:
            if nums[i] > nums[pivot]:
                if nums[j] < nums[pivot]:
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        
        tmp = nums[j]
        nums[j] = nums[pivot]
        nums[pivot] = tmp

        if j > left:
            quickSort(nums, left, j-1)
        if j < right:
            quickSort(nums, j+1, right)

        return nums

# Quick sort with an iterative method.
def quickSort2(nums: list[int]):
    pivot = 0
    right = len(nums) - 1
    stack = []
    stack.append(tuple((pivot,right)))
    
    while len(stack) > 0:
        pivot, right = stack.pop()
        i = pivot + 1
        j = right
        while i <= j:
            if nums[i] < nums[pivot]:
                i += 1
            elif nums[j] > nums[pivot]:
                j -= 1
            else:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        tmp = nums[pivot]
        nums[pivot] = nums[j]
        nums[j] = tmp
        
        if j < right:
            stack.append(tuple((j+1, right)))
        if j > pivot:
            stack.append(tuple((pivot, j-1)))
        
    return nums

    
example_arr = list(map(lambda x: random.randrange(1000000), range(1000000)))
start = time.time()
#result_arr = quickSort(example_arr, 0, len(example_arr)-1)
result_arr = quickSort2(example_arr)
print(result_arr)
end = time.time()

print(end - start)