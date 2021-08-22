#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 09:16:29 2021


"""
import os

import pandas as pd
import random
import numpy as np

"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, supermarketname):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name=supermarketname

   
    def get_time(self):
        """current time in HH:MM format,
        """        
        hour=7+self.minutes // 60
        min = self.minutes %60
        return f'current time is {hour:02}:{min:02}:00'
        

    def print_customers(self):
        
        """print all customers with the current time and id in CSV format.
        """
        for i in self.customers:
            print('the present time is {self.get_time())}, 
                  the customer ID is {i.id}, the state is {i.state}                         
                  ')        

    def next_minute(self):
        """propagates all customers to the next state.
        """
        for i in self.customers:
            i.move_next()
            #self.print_row(i)
        
    def add_new_customers(self):
        """randomly new customers come to the supermarket
        """    
        n=np.random.poisson(New_customers_per_minute)
        for i in len(n):  # or range(n):
            self.last_id += 1
            c=C_customer(self.last_id)
            self.customers.append(c)
           # self.print_row(c)
        
    def remove_exitsted_customers(self):
        """removes every customer that is not active any more.
        """
        self.customers=[i for i in self.customers if i.active()]
        #for i in customers:
         #   if i.active()==False:
          #      customers.remove(i)      
    
    def print_row(self, customer):
        """prints one row of CSV"""
        row = str(self) + ", " + str(customer)
        print(row)
    
     def __repr__(self):
        return print(f'now{self.get_time()}, there are {len(self.customers)} in the supermarket')
