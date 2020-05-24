def quicksort(array, left, right):
    """
    :type array: List [int]
    :type left: int
    :type right: int
    :rtype array: List [int]
    """
    i = left + 1
    k = right
    while i < k:
        while array[i] < array[left] and i < right:
            i += 1
        while array[k] >= array[left] and k > left:
            k -= 1
        if i < k:
            array[i], array[k] = array[k], array[i]
    array[left], array[k] = array[k], array[left]
    
    if left < k - 1:
        quicksort(array, left, k-1)
    if k + 1 < right:
        quicksort(array, k+1, right)
    return array