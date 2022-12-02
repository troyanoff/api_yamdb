def merge(arr, lf, mid, rg):
    len_arr = len(arr)
    if len_arr == 1:
        return arr

    left = merge(arr[lf:mid], lf, mid//2, mid)
    right = merge(arr[mid:rg], mid, rg//2, rg)
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
    # Your code
    # “ヽ(´▽｀)ノ”
    pass

def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

test()
