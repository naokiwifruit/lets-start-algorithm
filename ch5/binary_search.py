def binary_search(array, target):
    """
    :type array: List[int]
    :type target: int
    :rtype: str
    """
    head = 0
    tail = len(array) - 1
    while head <= tail:
        center = (head + tail) // 2
        if array[center] == target:
            return center
        elif array[center] < target:
            head = center + 1
        else:
            tail = center - 1
    else:
        return -1