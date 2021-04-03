from math import inf


def find_min(elements):
    _min = inf
    min_index = -1
    for i in range(len(elements)):
        if elements[i] < _min:
            _min = elements[i]
            min_index = i
    return min_index


def selection_sort(elements):
    for i in range(len(elements)-1):
        _min = find_min(elements[i + 1:]) + i + 1
        if elements[_min] < elements[i]:
            elements[i], elements[_min] = elements[_min], elements[i]


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 5, 1, 4, 25, 11, 32, 9]
    selection_sort(elements)
    print(elements)
