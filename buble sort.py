def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


tver = [78, 5, 66, -8, 132]
result = bubble_sort(tver)

print("Սկզբնական զանգվածը:", tver)
print("Սորտավորված զանգվածը:", result)