def partition(elements, start, end):
    pivot = elements[end]
    p_index = start
    for i in range(start, end):
        if elements[i] <= pivot:
            elements[p_index], elements[i] = elements[i], elements[p_index]
            p_index += 1
    elements[p_index], elements[end] = elements[end], elements[p_index]
    return p_index


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
