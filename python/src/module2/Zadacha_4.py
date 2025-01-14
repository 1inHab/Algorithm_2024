def merge(a, b, low, left_half, right_half):
    i = low
    k = low
    j = left_half + 1
    inversion_count = 0
    while i <= left_half and j <= right_half:
        if a[i] <= a[j]:
            b[k] = a[i]
            i = i + 1
        else:
            b[k] = a[j]
            j = j + 1
            inversion_count += (left_half - i + 1)
        k = k + 1
    while i <= left_half:
        b[k] = a[i]
        k = k + 1
        i = i + 1
    for i in range(low , right_half + 1):
        a[i] = b[i]
    return inversion_count

def merge_sort(a, b, low, large):
    if large <= low:
        return 0
    average = low + ((large - low) >> 1)
    inversion_count = 0
    inversion_count += merge_sort(a, b, low, average)
    inversion_count += merge_sort(a, b, average + 1, large)
    inversion_count += merge(a, b, low, average, large)
    return inversion_count

if __name__ == "__main__":
    s = int(input())
    if s == 1:
        a = int(input())
        print(0)
    else:
        a = list(map(int, input().split()))
        b = a.copy()
        print(merge_sort(a, b, 0, len(a) - 1))
    