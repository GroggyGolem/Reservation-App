'''
Created on Apr 30, 2020

@author: alita

'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import databaseModule
import buttons

class ReservationFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)   
        
                  
        #Create a label
        ttk.Label(self, text="Reservation Start Date").grid(column=0, row=0, sticky=tk.E)
        ttk.Label(self, text="Reservation End Date").grid(column=0, row=1, sticky=tk.E)
        ttk.Label(self, text="Would you like linens provided? ($15)").grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self, text="First Name").grid(column=0, row=3, sticky=tk.E)
        ttk.Label(self, text="Last Name").grid(column=0, row=4, sticky=tk.E)
        ttk.Label(self, text="Email").grid(column=0, row=5, sticky=tk.E)
        ttk.Label(self, text="Phone Number").grid(column=0, row=6, sticky=tk.E)
        ttk.Label(self, text="Address").grid(column=0, row=7, sticky=tk.E)
        ttk.Label(self, text="City").grid(column=0, row=8, sticky=tk.E)
        ttk.Label(self, text="State").grid(column=0, row=9, sticky=tk.E)
        ttk.Label(self, text="Zip Code").grid(column=0, row=10, sticky=tk.E)

        #Create entry field
        self.startDate = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.startDate).grid(column=1, row=0)
        self.endDate = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.endDate).grid(column=1, row=1)
        
        #extraServices
        linensTrue = IntVar()
        Checkbutton(self, text="Yes", variable=linensTrue).grid(row=2, column =1, sticky=tk.W )
        linensFalse = IntVar()
        Checkbutton(self, text="No", variable=linensFalse).grid(row=2, column=2, sticky=tk.W)
        
        self.customerFirstName = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerFirstName).grid(column=1, row=3)
        self.customerLastName = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerLastName).grid(column=1, row=4)
        self.customerEmail = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerEmail).grid(column=1, row=5)
        self.customerPhoneNumber = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerPhoneNumber).grid(column=1, row=6)
        self.customerAddress = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerAddress).grid(column=1, row=7)
        self.customerCity = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerCity).grid(column=1, row=8)
        self.customerState = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerState).grid(column=1, row=9)
        self.customerZip = tk.StringVar()
        ttk.Entry(self, width=25, textvariable=self.customerZip).grid(column=1, row=10)

        #Create Clearbutton
        ttk.Button(self, text="Clear", command=buttons.clear).grid(column=0, row = 13)

        #Create Savebutton    
        ttk.Button(self, text="Confirm", command=buttons.save).grid(column=1, row = 13)    
        
        #exit
        ttk.Button(self, text="Exit", command=buttons.exit).grid(column=2, row=13)
                    
        #Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

        
    def exit(self):
        root.destroy()   
   
  
#  -- main  --

databaseModule.createConnection("MRCreservations")   

root = tk.Tk()
root.title("Request Reservation")
root.geometry("500x500")
ReservationFrame(root)
root.mainloop()
 
#conn.close()    
