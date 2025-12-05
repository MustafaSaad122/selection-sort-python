def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


if __name__ == "__main__":
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
    ]
    
    for i, arr in enumerate(test_cases):
        sorted_arr = selection_sort(arr)
        print(f"Original: {arr}")
        print(f"Sorted:   {sorted_arr}")
        print("-" * 30)