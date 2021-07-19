# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:15:17 2021

@author: shubham.sharma1
"""


def ROTnEnc(n, s):
    l = list(s)
    for i in range(n):
        a = l.pop(-1)
        l.insert(0,a)
    return ''.join(l)



def ROTnDec(n, s):
    l = list(s)
    for i in range(n):
        a = l.pop(0)
        l.append(a)
    return ''.join(l)


if __name__ == '__main__':
    secretmsg = 'I am batman!'
    n = 5
    encmsg = ROTnEnc(n, secretmsg)
    print(encmsg)
    
    decmsg = ROTnDec(n, encmsg)
    print(decmsg)
