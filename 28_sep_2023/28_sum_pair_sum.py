def merge(a1, a2, arr):
    i, j, k = 0, 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            k += 1
            i += 1

        else:
            arr[k] = a2[j]
            j += 1
            k += 1
    
    while i < len(a1):
        arr[k] = a1[i]
        k += 1
        i += 1
    
    while j < len(a2):
        arr[k] = a2[j]
        k += 1
        j += 1


def sort_arr(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    sort_arr(a1)
    sort_arr(a2)
    merge(a1, a2, a)


def pair_sum(arr, s):
    # T --> O(N2)
    sort_arr(arr)
    output = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == s:
                output.append([arr[i], arr[j]])
    return output