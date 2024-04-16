import random

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


example_arr = list(map(lambda x: random.randrange(10), range(10)))
print(selection_sort(example_arr))