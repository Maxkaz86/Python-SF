# создаем форму для ввода данных и последующей проверке корректности данных
try:
    lists_ = list(map(int, (input('укажите числа через пробел: ').split())))
    num = int(input('Укажите произвольное целое число: '))
    if len(lists_) < 2:
        print('Данные введены без пробела')
        raise StopIteration
    if num < min(lists_) or num > max(lists_):
        print('Значение не соответствует условию')
        raise StopIteration
except ValueError:
    print('Повторите ввод данных')
    raise StopIteration

#  добавляем код для сортировки массива
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# добавляем поиск нужного индекса
def binary_search(L, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if L[middle-1] < element <= L[middle]:
        return middle - 1
    elif L[middle-1] < element >= L[middle]:
        return binary_search(L, element, middle+1, right)
    else:
        return binary_search(L, element, left, middle-1)


sort_list = merge_sort(lists_)
print(sort_list)
print(binary_search(sort_list, num, 0, len(lists_)))
