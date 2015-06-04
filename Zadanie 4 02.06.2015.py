__author__ = 'Dominik'
u"""
Realizacja zadania 4 polegajaca na znalezienie unikalnych bezwzglednie liczb w tablicy
przekazywanej funkcji absDistinct
"""
from random import randint

A=[]
u"""
Wypelnienie listy A elementami
"""
for i in range(0,2000):
    A.append(randint(-20,20))
print A

def absDistinct(A):
    list1=[]
    for i in range(0,len(A)):
        if not (A[i] and -A[i]) in list1:
            list1.append(A[i])
    return len(list1)

i=absDistinct(A)
print i