def hash_table(arrayD):
    """
    :type arrayD: List[int]
    :rtype arrayH List[int]
    """
    length = len(arrayD)
    length = int(1.5 * length)
    arrayH = [0 for _ in range(length)]
    i = 0
    while i < length:
        k = arrayD[i] % length
        while arrayH[k] != 0:
            k = (k + 1) % length
        arrayH[k] = arrayD[i]
        i += 1
    return arrayH