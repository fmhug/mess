# -*- coding: utf-8 -*-

import profile


class Person:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


def profile_attrs(person: Person):
    for i in range(100_000):
        name = person.name
        gender = person.gender
        age = person.age


def profile_getattr(person: Person):
    for i in range(100_000):
        name = getattr(person, 'name')
        gender = getattr(person, 'gender')
        age = getattr(person, 'age')


if __name__ == '__main__':
    # 对比直接访问对象属性和通过getattr方法获取属性的性能差异
    # 使用Macbook Pro 13 2017无Touch Bar测试
    p = Person('Tom', 'Male', 18)
    profile.run('profile_attrs(p)')    # 0.013 seconds，完胜
    profile.run('profile_getattr(p)')  # 0.731 seconds
