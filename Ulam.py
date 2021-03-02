#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:58:34 2021

@author: gotonis
"""

import matplotlib.pyplot as plt
import numpy as np


#naive spiral; maybe useful for non-polygonal spirals

#def squiral(max):
#    increment={
#            0:[1,0],
#            1:[0,1],
#            2:[-1,0],
#            3:[0,-1]}
#    x=0;
#    y=0;
#    curLineLength=1
#    curLinePoint=0
#    curDirection=0
#    L = [[0,0]];
#    for i in range(1,max):
#        x += increment[curDirection][0]
#        y += increment[curDirection][1]
#        curLinePoint += 1
#        if curLinePoint == curLineLength:
#            curLinePoint = 0
#            curLineLength += curDirection%2
#            curDirection = (curDirection+1)%4
#        L.append([x,y])
#    return np.array(L)

#TODO: consider rewriting in similar manner to triSpiral, then document
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

#TODO: comment (awaiting spiral() rewrite)
#TODO: use array comprehension rather than looping, return [t[],fig]
        #also, should have a version that just plots a set of points
        #rather than plotting the lines x -> f(x)
def plotSpiral(func,x,origin=1, **kwargs):
    fig,ax = plt.subplots()
    for i in x:
        if i >= origin and func(i) >= origin:
            t = np.array([spiral(i-origin+1),spiral(func(i)-origin+1)])
            ax.plot(t[:,0],t[:,1],**kwargs)
            ax.scatter(t[:,0],t[:,1])
            #ax.grid(1, which='both',markevery=1);
    fig



#TODO: consider doing a version that goes n units along the spiral rather than
    #just deforming the equilateral spiral
def triSpiral(n, a=np.array([1.0,0]),b=np.array([np.cos(2*np.pi/3),np.sin(2*np.pi/3)])):
    """Returns the coordinates for the point n on a triangle spiral
    
    Parameters
    ----------
    n : scalar
        The relative distance along the spiral
        Behavior is only guaranteed for nonnegative numbers
        non-integers are positioned along the line between integer points
        Spiral has vertices at a, a+2b, a+2b+3c, a+2b+3c+4a, ...
        Each integer increase in n adds a,b, or c to the position of n-1
    a: np.array(scalar[2]), optional
        The first vector for defining the spiral.
    b: np.array(scalar[2]), optional
        the second vector for defining the spiral.

        Default configuration of a,b,c is an equilateral triangle with side
        length 1.
        Due to erratic behavior, c is no longer settable, and is now defined
        in terms of a and b.
        This code assumes a+b+c=[0,0], which simplifies calculations.
        
    Returns
    -------
    np.array(scalar[2])
        a scalar[2] array representing the coordinates of the point n
        along the triangle spiral as defined by a,b,c.

    """
    
    c = -1*(a+b)
    
    if n <= 0:
        return np.array([0,0])
    if n <= 1:
        return n*a
    
    k = np.ceil((np.sqrt(8*n+1)-1)/6)-1
    #the point n is on the kth 'layer' of the spiral
    #print("{} is in layer {}".format(n,k))
    vertex = [0,0]
    dt = [0,0]
    #switch block breaks things into which 'side' of the layer n is in
    if n <= (9*k**2 + 9*k+2)/2:
        vertex = k*(c-a)
        t = (n - (9*k**2 + 3*k)/2)
        dt = t*a
        #print("{} units along segment 1".format(t))
    elif n <= (9*k**2 + 15*k)/2 + 3:
        vertex = k*(a-b)+a
        t = (n - (9*k**2 + 9*k + 2)/2)
        dt = t*b
        #print("{} units along segment 2".format(t))
    else:
        vertex = k*(b-c)+a+2*b
        t = (n- (9*k**2 + 15*k + 6)/2)
        dt = t*c
        #print("{} units along segment 3".format(t))
    return vertex+dt

def quickPlot1(func, dom, **kwargs):
    """evaluates func on dom then plots it
    
    Parameters:
    ----------
    
    func: scalar -> np.array([scalar,scalar])
        the function to plot
    dom: scalar[]
        the list of points on which to evaluate func
    kwargs: Line2D properties, optional. 
        keywords to pass into pyplot.plot()
        
    Returns
    -------
    list of Line2D
    pyplot.plot plot of the function evaluated over the domain
    
    """
    
    coords = np.stack([func(n) for n in dom])
    return plt.plot(coords[:,0],coords[:,1],**kwargs)
    
def quickPlot1S(func, dom, **kwargs):
    """evaluates func on dom then scatter plots it
    
    Parameters:
    ----------
    
    func: scalar -> np.array([scalar,scalar])
        the function to plot
    dom: scalar[]
        the list of points on which to evaluate func
    kwargs: Collection properties, optional. 
        keywords to pass into pyplot.plot()
        
    Returns
    -------
    PathCollection
    pyplot.scatter plot of the function evaluated over the domain
    
    """
    
    coords = np.stack([func(n) for n in dom])
    return plt.scatter(coords[:,0],coords[:,1],**kwargs)
    

def quickPlot2(func1, func2, dom, scatter=False, **kwargs):
    """plots lines between f1(x) and f2(x) for all x in dom
    
    Parameters:
    ----------
    
    func1: scalar -> np.array([scalar,scalar])
    func2: scalar -> np.array([scalar,scalar])
        the 2 functions to plot between
    dom: scalar[]
        the list of points on which to evaluate the func1,func2
    kwargs: Line2D properties, optional.
        keywords to pass into pyplot.plot
    
    """

    
    fig,ax = plt.subplots()
    for i in dom:
        t = np.array([func1(i),func2(i)])
        ax.plot(t[:,0],t[:,1],**kwargs)
        if scatter:
            ax.scatter(t[:,0],t[:,1])
    return fig,ax
        