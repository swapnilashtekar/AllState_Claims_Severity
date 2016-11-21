#!/usr/bin/python

import sys, os
import numpy as np
import pandas as pd

train = pd.read_csv('train.csv', ',')
test = pd.read_csv('test.csv', ',')

for column in list(train.select_dtypes(include=['object']).columns):
    #print train[column].nunique()
    #print test[column].nunique()
    if train[column].nunique() != test[column].nunique():
        print column + "\n"

