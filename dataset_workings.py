# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:46:36 2023

@author: markr
"""

# retrieve dataset and upload to panda dataframe. Also function to output a changed dataset

import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk

    
def load_csv(filepath):
    dataset = pd.read_csv(filepath)
    
    return dataset


def load_excel(filepath):
    dataset = pd.read_excel(filepath)

    return dataset

def load_json(filepath):
    dataset = pd.read_json(filepath)
    
    return dataset

def top_5(dataset):
    top5 = dataset.head()
    
    return top5

def bottom_5(dataset):
    bot5 = dataset.tail()
    
    return bot5

def data_info(dataset):
    datainfo = dataset.info()
    
    return datainfo

def row_count(dataset):
    rowcount = dataset.shape[0]
    
    return rowcount

def treeview_table(frame, dataset):
    
    tree_table = ttk.Treeview(frame)
    
    
        
    tree_table.delete(*tree_table.get_children())
    columns = list(dataset.columns)
    tree_table.__setitem__("column", columns)
    tree_table.__setitem__("show", "headings")

    for col in columns:
        tree_table.heading(col, text=col)

    df_rows = dataset.to_numpy().tolist()
    for row in df_rows:
        tree_table.insert("", "end", values=row)
        
    return tree_table