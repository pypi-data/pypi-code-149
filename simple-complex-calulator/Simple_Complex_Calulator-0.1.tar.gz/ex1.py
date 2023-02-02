#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:08:08 2023

@author: benoit.jomain
"""

def somme(t1,t2):
    return t1[0] + t2[0], t1[1] + t2[1]

def difference(t1,t2):
    return t1[0] - t2[0], t1[1] - t2[1]

def multiplication(t1,t2):
    return t1[0]*t2[0] -t1[1]*t2[1], t1[0]*t2[1] + t1[1]*t2[0]

def division(t1,t2):
    num = multiplication(t1, (t2[0],-t2[1]))
    den = float( t2[0]**2 + t2[1]**2)
    return num[0]/den, num[1]/den
if __name__=="__main__":
    #z= somme((12,3), (1,4))
    z= division((2,4), (3,5))
    print(z)