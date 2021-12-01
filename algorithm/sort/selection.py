# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F

# 趣味视频：https://www.bilibili.com/video/BV1xW411Y738


def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        # 记录最小值
        min_idx = i
        for j in range(i+1, length):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]


if __name__ == '__main__':
    lst1 = [21, 12, 3, 44, 5, 17, 9, 20, 20]
    selection_sort(lst1)
    print(lst1)
