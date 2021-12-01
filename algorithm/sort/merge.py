# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F

# 趣味视频：https://www.bilibili.com/video/BV1xW411Y7gY


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right
    return result


if __name__ == '__main__':
    lst1 = [21, 12, 3, 44, 5, 17, 9, 20]
    print(merge_sort(lst1))
