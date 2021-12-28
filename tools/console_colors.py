# coding: utf-8

black = 0   # 黑色
red = 1     # 红色
green = 2   # 绿色
yellow = 3  # 黄色
blue = 4    # 蓝色
purple = 5  # 紫色
cyan = 6    # 青色
white = 7   # 白色

colors = [
    black,
    red,
    green,
    yellow,
    blue,
    purple,
    cyan,
    white,
]

foregrounds = [30 + color for color in colors]  # 前景色
backgrounds = [40 + color for color in colors]  # 背景色
# ※ 表示不是所有终端都支持
forms = [
    0,  # 关闭所有格式，还原为初始状态
    1,  # 粗体/高亮显示
    2,  # 模糊（※）
    3,  # 斜体（※）
    4,  # 下划线（单线）
    5,  # 闪烁（慢）
    6,  # 闪烁（快）（※）
    7,  # 交换背景色与前景色
    8,  # 隐藏（伸手不见五指，啥也看不见）（※）
]


print(f'\033[0m让朕看看打印出来的是什么效果\t：\t0\033[0m')


def display_all():
    for form in forms:
        print('-' * 50)
        for fore in foregrounds:
            group = f'{form};{fore}m'
            print(f'\033[{group}让朕看看【前景色】打印出来的是什么效果\t：\t{group}\033[0m')

        for back in backgrounds:
            group = f'{form};{back}m'
            print(f'\033[{group}让朕看看【背景色】打印出来的是什么效果\t：\t{group}\033[0m')


def display_form_7():
    for fore in foregrounds:
        for back in backgrounds:
            group = f'1;7;{fore};{back}m'
            print(f'\033[{group}让朕看看【组合景色】打印出来的是什么效果\t：\t{group}\033[0m')


def display_white_background():
    for fore in foregrounds:
        group = f'1;{fore};40m'
        print(f'\033[{group}让朕看看【前景色】打印出来的是什么效果\t：\t{group}\033[0m')


def display_gray_background():
    for fore in foregrounds:
        group = f'1;{fore};100m'
        print(f'\033[{group}让朕看看【灰色背景】打印出来的是什么效果\t：\t{group}\033[0m')


display_all()