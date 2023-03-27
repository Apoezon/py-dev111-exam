

def partition(alist, start, end):
    """
    Вспомогательная функция к функции быстрой сортировки
    :param alist: лист кортежей по два элемента, где первый меньше второго
    :param start: стартовый элемент для сортировки
    :param end: конечный элемент для сортировки
    :return:
    """
    pivot = alist[(start+end) // 2]
    i = start
    j = end
    while i <= j:
        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i >= j:
            break
        alist[i], alist[j] = alist[j], alist[i]
        i += 1
        j -= 1
    return j

def quick_sort(container):
    """
    Функция ораганизует алгоритм быстрой сортировки листа заявок по времени начала аренды.
    :param container:
    :return:
    """
    if not container:
        return container

    def quicksort(alist, start, end):
        if start < end:
            p = partition(alist, start, end)
            quicksort(alist, start, p)
            quicksort(alist, p + 1, end)

    quicksort(container, 0, len(container) - 1)
    return container

def check_schedule(list:list):
    """
    Проверяет, хватит ли одной ракеты, чтобы удовлетворить все заявки.
    :param list: cписок заявок на использование ракеты в виде списка [(час_начала, час_окончания), ... ]
    :return: True, если нужна еще одна ракета, и False, если одной достаточно
    """
    result = False
    sorted_list = quick_sort(l)
    for i in range(1, len(sorted_list) - 1):

        if sorted_list[i - 1][1] > sorted_list[i][0]:
            result = result or True

    return result


l = [
    (12, 15),
    (9, 10),
    (11,  13),
    (8, 9),
    (23, 24),
    (18,21),
    (21,21),
    (21, 23)
]

print(check_schedule(l))
