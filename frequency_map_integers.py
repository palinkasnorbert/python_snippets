def freq_map(n):
    freq_map = {}
    while n > 0:
        digit = n % 10
        if digit not in freq_map:
            freq_map[digit] = 1
        else:
            freq_map[digit] += 1
        n = n // 10
    return freq_map


print(freq_map(99955444))
