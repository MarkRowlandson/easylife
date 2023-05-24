import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import pandas as pd 
import dataset_workings as dw

class SimpleData(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # set up base variables
        self.newDF = pd.DataFrame()
        self.changeDF = self.newDF
        self.errormsg = ""
        
        #set up the outer frame
        self.title("Dataset Shortcuts")
        self.geometry("800x700")

        self.resizable(0, 0)
               
        #notebook set up, needed for the tabs
        self.notebook = ttk.Notebook(self, width=800, height=600)
        
              
       
        
        
        
        
        
        # get data tab
    def create_getdata(self):
        
        getdata_tab = ttk.Frame(self.notebook, borderwidth=4, relief="ridge", width=600, height=400)
        
        getdata_tab.grid(column=0, row=0, columnspan=2, rowspan=6)
        
        getdata_button = tk.Button(getdata_tab, text="Upload Dataset", command=uploaddata
                                        , bg="lightblue", fg="white")
        get_data_label = ttk.Label(getdata_tab, text="Choose a Dataset to work with:", background="white"
                                        , foreground="black", justify="center")
        introduction_label = ttk.Label(getdata_tab, text="Explain what this tool can and can't do", background="lightgrey"
                                        , foreground="black", justify="center")      
        introduction_title = ttk.Label(getdata_tab, text="Introduction to Simplicity", background="lightgrey"
                                        , foreground="blue", justify="center", font=("Arial", 20))
        get_status_label = ttk.Label(getdata_tab, textvariable=self.errormsg, background="lightgrey"
                                        , foreground="blue", justify="center", font=("Arial", 16))
        
        introduction_title.grid(column=0, row=0, columnspan=2, padx=5)
        introduction_label.grid(column=0, row=1, rowspan=6, sticky=(N, W), padx=5, pady=5)
        get_data_label.grid(column=1, row=3, sticky=(N), padx=5, pady=5)
        getdata_button.grid(column=1, row=4, padx=5, pady=5)
        get_status_label.grid(column=1, row=5, padx=5, pady=5)
        
        
        notebook.columnconfigure(0, weight=1)
        notebook.rowconfigure(0, weight=1)
        getdata_tab.columnconfigure(0, weight=2)
        getdata_tab.columnconfigure(1, weight=1)
        getdata_tab.rowconfigure(0, weight=1)
        getdata_tab.rowconfigure(1, weight=3)
        getdata_tab.rowconfigure(2, weight=3)
        getdata_tab.rowconfigure(3, weight=3)
        getdata_tab.rowconfigure(4, weight=1)
        getdata_tab.rowconfigure(5, weight=1)
        
        # show data tab
    def create_showdata(self):
        #initialise text variables
        
        showdata_tab = ttk.Frame(self.notebook, borderwidth=4, relief="ridge", width=800, height=600)
        
        head = ""
        
        
        showdata_tab.grid(column=0, row=0, columnspan=2, rowspan=5, sticky=(N, S, E, W))
        
        download_data_button = tk.Button(showdata_tab, text="Save Dataset", command=savedata
                                               , bg="red", fg="black")
        show_data_label = ttk.Label(showdata_tab, text="Dataset Stats here", background="white"
                                        , foreground="black", font=("Arial", 20))
        
        head_label = ttk.Label(showdata_tab, text=head, background="white", foreground="black", justify="center")
        
        show_data_label.grid(column=0, row=0, columnspan=2, sticky=(N), padx=5)
        head_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W), padx=5)
        download_data_button.grid(column=1, row=4,  sticky=(N), padx=5)
        
        showdata_tab.columnconfigure(0, weight=1)
        showdata_tab.rowconfigure(0, weight=1)
        
    def create_datachoices(self):
        # commit changes tab
        
        data_choices_tab = ttk.Frame(self.notebook, borderwidth=4, relief="ridge", width=600, height=400)
        
        
        
        onevar = BooleanVar()
        twovar = BooleanVar()
        threevar = BooleanVar()

        onevar.set(False)
        twovar.set(False)
        threevar.set(False)

        one = ttk.Checkbutton(data_choices_tab, text="Remove Duplicates", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(data_choices_tab, text="Remove NA", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(data_choices_tab, text="Shuffle dataset", variable=threevar, onvalue=True)
        commit_change_button = tk.Button(data_choices_tab, text="Commit Changes", command=commitchange
                                              , bg="lightblue", fg="white")
       
        change_label = ttk.Label(data_choices_tab, text="Ability to adjust dataset here i.e. Remove duplicates"
                                      , background="white", foreground="black", justify="center")
        
        change_label.grid(column=0, row=0, columnspan=2, sticky=(N), padx=5)
        
        one.grid(column=0, row=1, columnspan=2, sticky=(N, S, E, W), padx=5)
        two.grid(column=0, row=2, columnspan=2, sticky=(N, S, E, W), padx=5)
        three.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W), padx=5)
        commit_change_button.grid(column=0, row=4, columnspan=2, sticky=(S, E, W), padx=5)
        
        
    def create_showchanges(self):
        
        showchanges_tab = ttk.Frame(self.notebook, borderwidth=4, relief="ridge", width=800, height=600)
        

        
    
        
    
    def uploaddata(self):
        file_path = fd.askopenfilenames( filetypes=[('All files', '*.*')])
        if file_path is not None:
            
            fpath = str(file_path)
            
            if fpath in ".csv":
                self.newDF = dw.load_csv(file_path)
                self.errormsg = "File from " + fpath + " uploaded"                
            elif fpath in ".xls":
                self.newDF = dw.load_excel(file_path)
                self.errormsg = "File from " + fpath + " uploaded"
            elif fpath in ".json":
                self.newDF = dw.load_json(file_path)
                self.errormsg = "File from " + fpath + " uploaded"
            else:
                self.errormsg = "File Type not supported."
            
        
            
    def savedata(self):
        pass

    def commitchange(self):
        pass


if __name__ == "__main__":
    simpledata = SimpleData()
    simpledata.mainloop()
