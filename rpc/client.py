# -*- coding: utf-8 -*-

import zerorpc


client = zerorpc.Client(
    connect_to='tcp://localhost:4242'
)

a = client.add(1, 2)
print(a)
m = client.mp(3, 4)
print(m)
