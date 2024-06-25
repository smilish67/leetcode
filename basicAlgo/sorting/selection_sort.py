import random
import time 

def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        if len(arr) <=1:
            break
        less_idx = i
        less_num = arr[i]
        for j in range(i+1, len(arr)):
            if arr[less_idx] > arr[j]:
                less_idx = j
                less_num = arr[less_idx]
        tmp = arr[i]
        arr[i] = arr[less_idx]
        arr[less_idx] = tmp 
    
    return arr


example_arr = list(map(lambda x: random.randrange(1000000), range(1000000)))
start = time.time()
selection_sort(example_arr)
end = time.time()

print(end - start)