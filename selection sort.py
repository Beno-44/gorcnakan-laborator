def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


tver = [78, 5, 66, -8, 132]
result = selection_sort(tver)

print("Սկզբնական:", tver)
print("Selection Sort արդյունք:", result)