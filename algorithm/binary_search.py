# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%90%9C%E5%B0%8B%E6%BC%94%E7%AE%97%E6%B3%95

# 二分查找
#
# 特性
# 1. 要求数组有序
# 2. 时间复杂度最坏是 O(log n)


def binary_search_with_while_loop(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            start = mid
    return -1


def binary_search_with_recursion(array, start, end, target):
    if start > end or not array:
        return -1
    mid = start + (end - start) // 2
    if array[mid] > target:
        return binary_search_with_recursion(array, start, mid, target)
    elif array[mid] < target:
        return binary_search_with_recursion(array, mid, end, target)
    return mid


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5, 7, 19, 20]
    print(binary_search_with_while_loop(lst1, 1))
    print(binary_search_with_while_loop(lst1, 19))
    print(binary_search_with_recursion(lst1, 0, len(lst1), 1))
    print(binary_search_with_recursion(lst1, 0, len(lst1), 19))
    print(binary_search_with_recursion([], 0, len(lst1), 19))
