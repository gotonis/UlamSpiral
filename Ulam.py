#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:58:34 2021

@author: gotonis
"""

import matplotlib.pyplot as plt
import numpy as np



def squiral(max):
    increment={
            0:[1,0],
            1:[0,1],
            2:[-1,0],
            3:[0,-1]}
    x=0;
    y=0;
    curLineLength=1
    curLinePoint=0
    curDirection=0
    L = [[0,0]];
    for i in range(1,max):
        x += increment[curDirection][0]
        y += increment[curDirection][1]
        curLinePoint += 1
        if curLinePoint == curLineLength:
            curLinePoint = 0
            curLineLength += curDirection%2
            curDirection = (curDirection+1)%4
        L.append([x,y])
    return np.array(L)


def spiral(n):
        k=np.ceil((np.sqrt(np.floor(n))-1)/2)
        t=2*k+1
        m=t**2 
        t=t-1
        if n>=m-t:
            return [round(k-(m-n),2),-k]
        m=m-t
        if n>=m-t:
            return [-k,round(-k+(m-n),2)]
        m=m-t
        if n>=m-t:
            return [round(-k+(m-n),2),k]
        return [k,round(k-(m-n-t),2)]

def plotSpiral(func,x,origin=1):
    fig,ax = plt.subplots()
    for i in x:
        if i > origin and func(i) > origin:
            t = np.array([spiral(i-origin+1),spiral(func(i)-origin+1)])
            ax.plot(t[:,0],t[:,1])
    fig
    
