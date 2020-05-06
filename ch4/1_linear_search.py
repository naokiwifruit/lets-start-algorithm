def linear_search(array, target):
    """
    :type array: List[int]
    :type target: int
    :rtype: str
    """
    length = len(array)
    i = 0
    while i < length:
        if array[i] == target:
            return i
        else:
            i += 1
    else:
        return -1