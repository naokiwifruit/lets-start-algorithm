def hash_search(arrayH, target):
    """
    :type arrayH: List[int]
    :type target: int
    :rtype k: int
    """
    size = len(arrayH)
    k = target % size
    while arrayH[k] != 0:
        if arrayH[k] == target:
            return k
        else:
            k = (k + 1) % size
    else:
        return -1