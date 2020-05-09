def hash_table(arrayD):
    """
    :type arrayD: List[int]
    :rtype arrayH List[int]
    """
    length = len(arrayD)
    size = int(1.5 * length)
    arrayH = [0 for _ in range(size)]
    i = 0
    while i < length:
        k = arrayD[i] % size
        while arrayH[k] != 0:
            k = (k + 1) % size
        arrayH[k] = arrayD[i]
        i += 1
    return arrayH