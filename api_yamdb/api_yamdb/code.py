def merge(arr, lf, mid, rg):
    len_arr = len(arr)
    left = arr[:mid]
    right = arr[mid:]
    len_left = len(left)
    len_right = len(right)
    l,r,k = 0, 0, 0
    result = [None] * len_arr
    while l < len_left and r < len_right:
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while l < len_left: 
        result[k] = left[l]
        l += 1
        k += 1  
    while r < len_right: 
        result[k] = right[r]
        r += 1
        k += 1
  
    return result


def merge_sort(arr, lf, rg):
    len_arr = len(arr)
    rg = len_arr
    mid = rg//2
    if len_arr == 1:
        return arr

    left = merge_sort(arr[:mid], lf, mid)
    right = merge_sort(arr[mid:], 0, rg)
    len_left = len(left)
    len_right = len(right)
    left_right = left+right
    len_lr = len(left_right)
    if len_arr == len(Array):
        for i in range(len_arr):
            Array[i] = arr[i]
    else:
        return merge(left_right,0,len_lr//2, len_lr)

