# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:13:43 2023

@author: markr
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
import pandas as pd 
import dataset_workings as dw


class SimpleData(tk.Tk):
    def __init__(self):
        
        super().__init__()
        
        global newDF, errormsg, changeDF, showToggle, changeToggle
        
        newDF = pd.DataFrame()
        changeDF = newDF
        errormsg = tk.StringVar()
        showToggle = 0
        changeToggle = 0
        
        
       
        #set up the outer frame
        self.title("Dataset Shortcuts")
        self.geometry("800x600")

        self.resizable(0, 0)
               
        #notebook set up, needed for the tabs
        self.notebook = ttk.Notebook(self, width=800, height=500)
        
        
        self.getdata = Get_Data(self.notebook)
        self.showdata = Show_Data(self.notebook)
        self.datachoices = Data_Changes(self.notebook)
        self.showchange = Show_Changes(self.notebook)
        
        
        self.notebook.add(self.getdata, text="Get Dataset")
        self.notebook.add(self.showdata, text="Discovery")
        self.notebook.add(self.datachoices, text="Possible Changes")
        self.notebook.add(self.showchange, text="Show Changes")

        self.notebook.rowconfigure(0,weight=1)
        self.notebook.columnconfigure(0,weight=1)
        self.notebook.grid()
        
    def refresh(self, toggle):
        if toggle == 1:
            self.showdata.destroy()
            self.showchange.destroy()
            Show_Data(SimpleData.notebook)
            Show_Changes(SimpleData.notebook)
            self.notebook.grid()
        # self.notebook.pack(fill=tk.BOTH, expand=True)

class Get_Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        
        
        global errormsg
        
        getdata_tab = ttk.Frame(self, borderwidth=4, relief="ridge", width=800, height=500)
        
        getdata_tab.columnconfigure(0, weight=2)
        getdata_tab.columnconfigure(1, weight=1)
        getdata_tab.rowconfigure(0, weight=1)
        
        
        getdata_tab.grid(column=0, row=0, columnspan=2, rowspan=4, padx=10,pady=100)
        
        getdata_button = tk.Button(getdata_tab, text="Upload Dataset", command=self.uploaddata
                                        , bg="lightgreen", fg="white")
        get_data_label = ttk.Label(getdata_tab, text="Choose a Dataset to work with:", background="white"
                                        , foreground="black", justify="center",font=("Arial", 12))
        introduction_label = ttk.Label(getdata_tab, text="""Upload the dataset that you need to investigate.
Common data specifics will show on the Discovery Tab.
The possible changes tab will automatically process any changes
and allow you to download the changed dataset in csv format.
You can compare the changes to the original data in the Show Changes tab"""
                                            , background="white", foreground="black",font=("Arial", 12)
                                            , justify="left")      
        introduction_title = ttk.Label(getdata_tab, text="Introduction to Simplicity", background="lightgrey"
                                        , foreground="blue", justify="center", font=("Arial", 20))
        get_status_label = ttk.Label(getdata_tab, textvariable=errormsg, background="lightgrey"
                                        , foreground="blue", justify="center", font=("Arial", 8))
        
        introduction_title.grid(column=0, row=0, columnspan=2, padx=5)
        introduction_label.grid(column=0, row=1, rowspan=3, sticky=(tk.N, tk.W), padx=5, pady=5)
        get_data_label.grid(column=1, row=1, sticky=(tk.N), padx=5, pady=5)
        getdata_button.grid(column=1, row=2, padx=5, pady=5)
        get_status_label.grid(column=1, row=3, padx=5, pady=5)
        SimpleData.refresh(parent,showToggle)
        
        
    def uploaddata(self):
        # file_path = fd.askopenfilenames( title='Open a file',initialdir='/',filetypes=[('All files', '*.*')])
        # if file_path is not None:
            
        global newDF, errormsg, changeDF, showToggle
        
        ftypes = [ ('All files', '*')]
        dlg = fd.Open(self, filetypes = ftypes)
        fpath = dlg.show()
        if fpath != '':
            path_object = Path(fpath)
            file_name = path_object.name
            
            if ".csv" in fpath:
                newDF = dw.load_csv(fpath)
                errormsg.set(  file_name + " uploaded" )
                showToggle = 1
            elif ".xls" in fpath:
                newDF = dw.load_excel(fpath)
                errormsg.set( file_name + " uploaded")
                showToggle=1
            elif ".json" in fpath:
                newDF = dw.load_json(fpath)
                errormsg.set( file_name + " uploaded")
                showToggle=1
            else:
                errormsg.set( "File Type not supported.")
                
                   
        else:
            errormsg.set( "Not sure whats going on here!")
        
        SimpleData.refresh(self.parent, showToggle)
        
        
class Show_Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        # show data tab
        
        
        
        global newDF, showToggle
        
        if showToggle == 1:
            
            showdata_tab = ttk.Frame(self, borderwidth=4, relief="ridge", width=800, height=600)
        
            head_frame = ttk.Frame(showdata_tab, borderwidth=4, relief="ridge", width=800, height=100)
               
            tail_frame = ttk.Frame(showdata_tab, borderwidth=4, relief="ridge", width=800, height=100)
        
        
            showdata_tab.columnconfigure(0,weight=1)
            showdata_tab.columnconfigure(1,weight=1)
            showdata_tab.columnconfigure(2,weight=1)
            showdata_tab.columnconfigure(3,weight=2)
            showdata_tab.rowconfigure(0,weight=1)
            showdata_tab.rowconfigure(4,weight=2)
            showdata_tab.rowconfigure(5,weight=2)        
        
            showdata_tab.grid(column=0, row=0, columnspan=4, rowspan=6, sticky=(N, S, E, W))
        
            head_frame.rowconfigure(0,weight=1)
            head_frame.rowconfigure(1,weight=3)
            head_frame.grid(column=0, row=4, columnspan=5)
        
            tail_frame.rowconfigure(0,weight=1)
            tail_frame.rowconfigure(1,weight=3)
            tail_frame.grid(column=0, row=5, columnspan=5)
        
        
        
        
            download_data_button = tk.Button(showdata_tab, text="Save Dataset", command=self.savedata
                                               , bg="red", fg="black")
            show_data_label = ttk.Label(showdata_tab, text="Dataset Stats here", background="white"
                                        , foreground="black", font=("Arial", 20))
        
            head_label = ttk.Label(head_frame, text="Head", background="white", foreground="black", justify="center")
        
            head_text = dw.treeview_table(head_frame,dw.top_5(newDF))
        
        
            tail_text = dw.treeview_table(tail_frame,dw.bottom_5(newDF))
                
            show_data_label.grid(column=0, row=0, columnspan=2, sticky=(N), padx=5)
            head_label.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W), padx=5)
            head_text.grid(column=0, row=0, sticky=(S), padx=5)
            tail_text.grid(column=0, row=0, sticky=(S), padx=5)
        
            download_data_button.grid(column=1, row=4,  sticky=(N), padx=5)
        else:
            pass
    
    def savedata(self):
        pass
       


class Data_Changes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # commit changes tab
        data_choices_tab = ttk.Frame(self, borderwidth=4, relief="ridge", width=600, height=400)
        data_choices_tab.grid(column=0, row=0, rowspan=4, padx=10,pady=100)
        
        
        onevar = tk.BooleanVar()
        twovar = tk.BooleanVar()
        threevar = tk.BooleanVar()

        onevar.set(False)
        twovar.set(False)
        threevar.set(False)

        one = ttk.Checkbutton(data_choices_tab, text="Remove Duplicates", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(data_choices_tab, text="Remove NA", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(data_choices_tab, text="Shuffle dataset", variable=threevar, onvalue=True)
        commit_change_button = tk.Button(data_choices_tab, text="Commit Changes", command=self.commitchange
                                              , bg="lightblue", fg="white")
       
        change_label = ttk.Label(data_choices_tab, text="Ability to adjust dataset here i.e. Remove duplicates"
                                      , background="white", foreground="black", justify="center")
        
        change_label.grid(column=0, row=0, columnspan=2, sticky=(N), padx=5)
        
        one.grid(column=0, row=1, columnspan=2, sticky=(N, S, E, W), padx=5)
        two.grid(column=0, row=2, columnspan=2, sticky=(N, S, E, W), padx=5)
        three.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W), padx=5)
        commit_change_button.grid(column=0, row=4, columnspan=2, sticky=(S, E, W), padx=5)
        
    
    def commitchange(self):
        pass
       
        
class Show_Changes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        showdata_tab = ttk.Frame(self, borderwidth=4, relief="ridge", width=600, height=400)
        showdata_tab.grid(column=0, row=0, rowspan=4, padx=10,pady=100)
        
    pass
          
       
        
       
        
    
        
  
    
    
     
            
    

    
    
   




if __name__ == "__main__":
    simpledata = SimpleData()
    simpledata.mainloop()


