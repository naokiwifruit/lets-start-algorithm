def sieve_of_eratosthenes(n):
    """
    :type n: int
    :rtype prime_numbers: List [int]
    """
    array = [1 for i in range(n+1)]
    prime_numbers = []
    k = 2
    while k * k <= n:
        i = k
        while i <= n / k:
            array[k*i] = 0
            i += 1
        while True:
            k += 1
            if array[k] == 1:
                break
    i = 2
    while i <= n:
        if array[i] == 1:
            prime_numbers.append(i)
        i += 1
    return prime_numbers