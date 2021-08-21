#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 09:16:29 2021

@author: baodong
"""

import numpy as np


class Customer:
    '''
    The class customer is a blueprint for a customer in the supermarket.
    Arrtibutes
    ---------
    name
    state
    budget
    Methods
    -------    
    '''
    import pandas as pd
    import random
    import numpy as np

    ct_pro=pd.read_csv('./tr_prob.csv')    
    
    def __init__(self, id):
        self.id=id
        self.state='fruit'
        
    def move_next(self):
        '''
        propagates the customer to the next state.
        Return nothing
        '''
        self.state =np.random.choices(list(self.ct_pro.index),weights=self.ct_pro[self.state])[0]
      
    def __repr__(self):
        return f'Customer{self.id}in {self.state}'
    
    def active(self):
        ''''check whether the customer is still in supermarket'''
        return self.state != "checkout"

if __name__ == "__main__":
    c = Customer(1)
    for i in range(10):
        c.__repr__()
        c.move_next()
        c.__repr__()