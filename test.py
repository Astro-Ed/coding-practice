# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:15:09 2022

@author: jose
"""

import pandas as pd
import os
import h5py
import numpy as np

#file_name_h5 = os.path.join('tabular_data.h5')
#h5f = h5py.File(file_name_h5,'r')
#X_tab = h5f['dataset_tab'][:]
#h5f.close()



with h5py.File('tabular_data.h5', "r") as f:
    # Print all root level object names (aka keys) 
    # these can be group or dataset names 
    print("Keys: %s" % f.keys())
    # get first object name/key; may or may NOT be a group
    a_group_key = list(f.keys())[0]

    # get the object type for a_group_key: usually group or dataset
    print(type(f[a_group_key])) 

    # If a_group_key is a group name, 
    # this gets the object names in the group and returns as a list
    data = list(f[a_group_key])

    # If a_group_key is a dataset name, 
    # this gets the dataset values and returns as a list
    data = list(f[a_group_key])
    # preferred methods to get dataset values:
    ds_obj = f[a_group_key]      # returns as a h5py dataset object
    ds_arr = f[a_group_key][()]  # returns as a numpy array


file = open("sample.txt", "w+")
content = str(np.array(ds_arr))
file.write(content)
file.close()

file = open("sample.txt", "r")
content = file.read()