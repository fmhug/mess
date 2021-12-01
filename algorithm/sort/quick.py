# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F

# 趣味视频：https://www.bilibili.com/video/BV1xW411Y7g3

# 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

# 步骤为：
# 1. 挑选基准值：从数列中挑出一个元素，称为“基准”（pivot），
# 2. 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。
#         在这个分割结束之后，对基准值的排序就已经完成，
# 3. 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。


# 一行实现快排，易读性差
quick_sort_with_lambda = lambda array: array if len(array) <= 1 \
    else quick_sort_with_lambda([item for item in array[1:] if item <= array[0]]) + \
         [array[0]] + quick_sort_with_lambda([item for item in array[1:] if item > array[0]])


# 使用递归实现快拍
def quick_sort_with_recursion(array, start=None, end=None):
    # 减少调用时的参数输入
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    if start >= end:
        return

    left = start
    right = end
    # 选择基准
    pivot = array[start]

    while left < right:
        # 从右边找比基准元素小的数
        while left < right and pivot <= array[right]:
            right -= 1
        # right 一直在向左移，直到移到某个比基准小的元素，然后 left 从当前位置开始
        array[left] = array[right]

        # 从左边找比基准元素大的数
        while left < right and pivot > array[left]:
            left += 1
        array[right] = array[left]

    # 基准元素的位置确定，此时它左边的数都比它小，右边的数都比它大
    array[left] = pivot

    quick_sort_with_recursion(array, start, left - 1)
    quick_sort_with_recursion(array, left + 1, right)


if __name__ == '__main__':
    lst1 = [21, 12, 3, 44, 5, 17, 9, 20]
    print(quick_sort_with_lambda(lst1))
    quick_sort_with_recursion(lst1)
    print(lst1)
