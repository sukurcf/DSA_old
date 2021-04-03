def shell_sort(elements):
    gap = len(elements) // 2
    while gap > 0:
        for i in range(gap, len(elements)):
            anchor = elements[i]
            j = i
            while anchor < elements[j - gap] and j >= gap:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        gap //= 2


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)
