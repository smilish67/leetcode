import random
import time

def merge_sort(arr: list[int]):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    
    return merge(left, right)


def merge(left: list[int], right: list[int]):
    i = 0
    j = 0
    arr = []
    while i<len(left) and j<len(right):
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i += 1
            
    while i<len(left):
        arr.append(left[i])
        i += 1
        
    while j<len(right):
        arr.append(right[j])
        j += 1
    return arr
                

example_arr = list(map(lambda x: random.randrange(1000000), range(1000000)))
start = time.time()
merge_sort(example_arr)
end = time.time()

print(end - start)
    