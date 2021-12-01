# -*- coding: utf-8 -*-

# https://zh.wikipedia.org/wiki/%E4%BD%8D%E5%9B%BE


class Bitmap:

    def __init__(self, length: int = None):
        if length is None:
            length = 2 ** 10
        self.length = length
        self.positive_bitmap = [0 for i in range(self.length)]
        self.negative_bitmap = [0 for i in range(self.length)]

    def load(self, lst):
        """
        装载待排序数组
        """
        for i in lst:
            self.add(i)

    def add(self, n):
        """

        """
        bitmap = self.positive_bitmap if n >= 0 else self.negative_bitmap
        bitmap[n] = 1

    def clean(self, n):
        self.positive_bitmap[n] = 0

    def sort(self):
        result = []
        for i, j in enumerate(self.negative_bitmap):
            if j:
                num = i-self.length
                result.append(num)

        for i, j in enumerate(self.positive_bitmap):
            if j:
                result.append(i)

        return result


if __name__ == '__main__':
    bit = Bitmap(128)
    nums = [31, 92, 1, 4, 19, 66, -1, -8]
    bit.load(nums)
    print(bit.sort())
