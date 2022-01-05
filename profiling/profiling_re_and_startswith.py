# coding: utf-8

import re
import profile


phrase = 'Let me, your sacred emperor, see see.'
times = 50_000


def test_re():
    for i in range(times):
        res = re.match(r'Let', phrase)


def test_starts():
    for i in range(times):
        res = phrase.startswith('Let')


if __name__ == '__main__':
    profile.run('test_re()')
    profile.run('test_starts()')
