# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:49:41 2021

@author: shubham.sharma1
"""




def Rotn(n,s):
    a = ''
    for i in s:
        x = chr(ord(i) + n)
        a = a + x
    return(a)    
     


def Rotdec(n, a):
    b= ''
    for i in a:
        y= chr(ord(i) - n)
        # print(i, y)
        b= b + y
    return(b)    
      
        
    
    
if __name__ == '__main__': 
    import sys
    try:
        s = sys.argv[1]
    except Exception:
        s = input("Enter a message: ")
        
    n = 2
    c = Rotn(n,s)
    print(c)
    d = Rotdec(n, c) 
    print(d)
    
    
    

         

    


            
        