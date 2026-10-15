def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Փորձարկում
tver = [78, 5, 66, -8, 132]
result = quick_sort(tver)

print("Սկզբնական:", tver)
print("Quick Sort արդյունք:", result)