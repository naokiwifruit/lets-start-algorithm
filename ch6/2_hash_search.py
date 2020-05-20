def hash_search(arrayH, target):
    """
    :type arrayH: List[int]
    :type target: int
    :rtype k: int
    """
    length = len(arrayH)
    k = target % length
    while arrayH[k] != 0:
        if arrayH[k] == target:
            return k
        else:
            k = (k + 1) % length
    else:
        return -1