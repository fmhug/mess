# -*- coding: utf-8 -*-

# 实现进制间互相转换

import string

# Base 2 - 62 conversion characters
letters = string.digits + string.ascii_letters
# Base 63 - 64 conversion characters
letters += '+/'
# Used to convert other base to base 10
decode_base_map = {j: i for i, j in enumerate(letters)}


def bs10_to_n(num: int, base: int = 16):
    """
    用于将10进制转换为其他进制
    """
    if base < 2:
        raise ValueError('Base cannot be less than 0')
    result = []
    temp = num
    while True:
        if temp == 0:
            result.append('0')
            break
        else:
            result.append(letters[temp % base])
            temp //= base

    return ''.join([x for x in reversed(result)])


def others_to_bs10(s: str, base: int):
    """
    用于将其他进制转换为10进制数值
    """
    if base < 2:
        raise ValueError('Base cannot be less than 0')
    result = 0
    for i, j in enumerate(s):
        result *= base
        result += decode_base_map[j]
    return result


if __name__ == '__main__':
    num = 125
    base_2 = bs10_to_n(num, 2)
    base_16 = bs10_to_n(num, 16)
    base_32 = bs10_to_n(num, 32)
    base_62 = bs10_to_n(num, 62)
    base_64 = bs10_to_n(num, 64)
    assert others_to_bs10(base_2, 2) == num
    assert others_to_bs10(base_16, 16) == num
    assert others_to_bs10(base_32, 32) == num
    assert others_to_bs10(base_62, 62) == num
    assert others_to_bs10(base_64, 64) == num
