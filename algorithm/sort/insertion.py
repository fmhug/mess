# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F

# 趣味视频：https://www.bilibili.com/video/BV1xW411Y73Z

# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置后
# 6. 重复步骤2~5


def insertion_sort(array):
    for i in range(1, len(array)):
        # 当前做比较的元素
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current


def insertion_sort2(array):
    for i in range(1, len(array)):
        # 插入排序（逆序）
        for j in range(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            array[j], array[j - 1] = array[j - 1], array[j]


if __name__ == '__main__':
    lst1 = [21, 12, 3, 44, 5, 17, 9, 20]
    # insertion_sort(lst1)
    insertion_sort2(lst1)
    print(lst1)
