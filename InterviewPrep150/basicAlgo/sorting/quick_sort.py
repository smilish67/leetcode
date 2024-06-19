import random
import time

def quick_sort(arr: list[int], start:int, end:int):
    # Defining proper out points of recursive function is important.
    if start == end or end < 0 or start > end:
        return
    
    pivot = start
    i = start+1
    j = end
    
    while i<=j:
        if arr[i] > arr[pivot]:
            if arr[j] < arr[pivot]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
            
    tmp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = tmp
    
    quick_sort(arr, start, j-1)
    quick_sort(arr, j+1, end)
    
    return arr

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

example_arr = list(map(lambda x: random.randrange(1000000), range(1000000)))
start = time.time()
result_arr = quickSort(example_arr, 0, len(example_arr)-1)
end = time.time()

print(end - start)