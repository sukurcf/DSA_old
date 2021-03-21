from pprint import pprint


def bubble_sort(elements):
    for i in range(len(elements) - 1):
        swapped = False
        for j in range(len(elements) - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements


def bubble_sort_with_key(elements, key):
    for i in range(len(elements) - 1):
        swapped = False
        for j in range(len(elements) - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements


print(bubble_sort([5, 9, 2, 1, 67, 34, 88, 34]))
pprint(bubble_sort_with_key([
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'mona', 'transaction_amount': 10, 'device': 'iphone-10'},
    {'name': 'mona', 'transaction_amount': 100, 'device': 'iphone-10'},
    {'name': 'mona', 'transaction_amount': 1, 'device': 'iphone-10'},
], 'transaction_amount'))
