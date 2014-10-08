# -*- coding: utf-8 -*-
"""
Fonctions mathématiques de la mort
"""

def myfunction(x):
  """
  A powerful function that computes :math:`y=x^2`
  
  :param x: the x value
  :type x: float
  :rtype: float
  
  >>> x = 5
  >>> y = myfunction(x)
  >>> y
  25
  >>> print "AMAZING !!!"
  AMAZING !!!
  >>> 
  
  .. note::
  
   This function is too simple
   
  .. image:: images/toto.jpg
  """
  return x**2


x = 5
y = myfunction(x)