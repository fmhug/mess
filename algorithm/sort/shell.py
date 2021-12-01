# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F

# 趣味视频：https://www.bilibili.com/video/BV1xW411Y7gf


def shell_sort(array):
    n = len(array)
    # 初始步長
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步長進行插入排序
            temp = array[i]
            j = i
            # 插入排序
            while j >= 0 and j - gap >= 0 and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        # 得到新的步長
        gap = gap // 2
    return array


if __name__ == '__main__':
    lst1 = [21, 12, 3, 44, 5, 17, 9, 20]
    shell_sort(lst1)
    print(lst1)
