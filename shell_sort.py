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


def shell_sort_remove_duplicates(elements):
    size = len(elements)
    div = 2
    gap = size // div

    while gap > 0:
        indexs_to_delete = []
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while anchor <= elements[j - gap] and j >= gap:
                if anchor == elements[j - gap]:
                    indexs_to_delete.append(j)
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        if indexs_to_delete:
            for i in indexs_to_delete:
                del elements[i]
        size = len(elements)
        div *= 2
        gap = size // div


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9, 9]
    shell_sort_remove_duplicates(elements)
    print(elements)
