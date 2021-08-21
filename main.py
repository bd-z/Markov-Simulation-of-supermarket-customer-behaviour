#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:28:42 2021

@author: baodong
"""
import numpy as np
import C_customer
import C_supermarket

start_time='2021-8-21 7:00'
end_time ='2021-8-21 7:30'
timesteps = pd.date_range(start_time, ent_time, freq='1min')


shop=C_supermarket('star-star')
for ts in timesteps:
    shop.next_minute()
    # number of new customer entry to shop
    shop.add_new_customers()
    shop.remove_exited_customers()
    shop.print_customers()
    
    