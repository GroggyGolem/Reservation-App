
import tkinter as tk
from tkinter import *
from tkinter import ttk
import databaseModule
from databaseModule import createConnection
import random
from datetime import date
import calendar


class ReservationFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)   
      

          
        #Create a label
        ttk.Label(self, text="Reservation Start Date:").grid(column=0, row=0, sticky=tk.E)
        ttk.Label(self, text="Reservation End Date:").grid(column=0, row=1, sticky=tk.E)
        ttk.Label(self, text="Would you like linens provided? ($15)").grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self, text="First Name:").grid(column=0, row=3, sticky=tk.E)
        ttk.Label(self, text="Last Name:").grid(column=0, row=4, sticky=tk.E)
        ttk.Label(self, text="Email:").grid(column=0, row=5, sticky=tk.E)
        ttk.Label(self, text="Phone Number:").grid(column=0, row=6, sticky=tk.E)
        ttk.Label(self, text="Address:").grid(column=0, row=7, sticky=tk.E)
        ttk.Label(self, text="City:").grid(column=0, row=8, sticky=tk.E)
        ttk.Label(self, text="State:").grid(column=0, row=9, sticky=tk.E)
        ttk.Label(self, text="Zip Code:").grid(column=0, row=10, sticky=tk.E)

        #Create entry field
        self.startDay = tk.IntVar()
        ttk.Entry(self, width=10, textvariable=self.startDay).grid(column=1, row=0, sticky=tk.W)
        self.startMonth = tk.IntVar()
        ttk.Entry(self, width=10, textvariable=self.startMonth).grid(column=1, row=0, sticky=tk.E)
        self.startYear = tk.IntVar()
        ttk.Entry(self, width=10, textvariable=self.startYear).grid(column=2, row=0)
        
        self.startDay.set('DD')
        self.startMonth.set('MM')
        self.startYear.set(date.today().year)

                                  
        self.endDay = tk.IntVar()
        ttk.Entry(self, width=10, textvariable=self.endDay).grid(column=1, row=1, sticky=tk.W)
        self.endMonth = tk.IntVar()
        ttk.Entry(self, width=10, textvariable=self.endMonth).grid(column=1, row=1, sticky=tk.E)
        
        self.endDay.set('DD')
        self.endMonth.set('MM')
        
        
        #extraServices
        global linensTrue
        linensTrue = IntVar()
        Checkbutton(self, text="Yes", variable=linensTrue).grid(row=2, column =1, sticky=tk.W )
        linensFalse = IntVar()
        Checkbutton(self, text="No", variable=linensFalse).grid(row=2, column=1, sticky=tk.E)
        
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
        ttk.Button(self, text="Clear", command=self.clear).grid(column=0, row = 13)

        #Create Savebutton    
        ttk.Button(self, text="Confirm", command=self.save).grid(column=1, row = 13)    
        
        #exit
        ttk.Button(self, text="Exit", command=self.exit).grid(column=2, row=13)
                    
        #Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

        
    def exit(self):
        root.destroy()  
    
    def clear(self):
        print("Customer First Name", self.customerFirstName.get())
        self.customerFirstName.set("")
                
        print("Customer Last Name", self.customerLastName.get())
        self.customerLastName.set("")
                
        print("Customer Email", self.customerEmail.get())
        self.customerEmail.set("")
                
        print("Customer Phone Number", self.customerPhoneNumber.get())
        self.customerPhoneNumber.set("")
                
        print("Customer Address", self.customerAddress.get())
        self.customerAddress.set("")
                
        print("Customer City", self.customerCity.get())
        self.customerCity.set("")
                
        print("Customer State", self.customerState.get())
        self.customerState.set("")
                
        print("Customer Zip", self.customerZip.get())
        self.customerZip.set("")
                
        
        self.startDate = tk.StringVar()
        start = self.startDay, "/" , self.startMonth, "/", self.startYear
        self.startDate.set(start)
        self.endDate = tk.StringVar()
        end = self.endDay, "/" , self.endMonth, "/", self.startYear
        self.endDate.set(end)
        print("Start Date", self.startDate.get())
        self.startDate.set("")
                
        print("End Date", self.endDate.get())
        self.endDate.set("")                
            
    def save(self):    
        #create Connection to database 
        databaseModule.main()    
        database = r"C:\sqlite\db\reservation.db"
        conn = createConnection(database)
        c = conn.cursor()
        
        self.startDate = tk.StringVar()
        start = self.startDay.get(), "/" , self.startMonth.get(), "/", self.startYear.get()
        self.startDate.set(start)
        self.endDate = tk.StringVar()
        end = self.endDay.get(), "/" , self.endMonth.get(), "/", self.startYear.get()
        self.endDate.set(end)
        
        
        #create random Customer ID
        y = TRUE
        while y is TRUE:
            stringCusID = ''
            for x in range(4):
                randomDigit = random.choice('0123456789')
                stringCusID += randomDigit
            custID = int(stringCusID)
            #checks to see if id already exists in table
            c.execute("SELECT customerId FROM customer where customerId = :randomID LIMIT 1", {'randomID':custID})
            if c.fetchone():
                y = TRUE
            else:
                y = FALSE
                
        #insert into table
        c.execute("INSERT INTO customer VALUES (:customerId, :firstName, :lastName, :email, :phone, :address, :salesDate)",
                  {'customerId':custID, 
                   'firstName':self.customerFirstName.get(), 
                   'lastName':self.customerLastName.get(),
                   'email':self.customerEmail.get(),
                   'phone':self.customerPhoneNumber.get(),
                   'address':self.customerAddress.get(),
                   'salesDate':self.startDate.get()
                   }
                  )        
        #Creating SaleID
        y = TRUE
        while y is TRUE:
            stringSaleID= ''
            for x in range(4):
                randomDigit = random.choice('0123456789')
                stringSaleID += randomDigit
            saleID = int(stringSaleID)
            #checks to see if id already exists in table
            c.execute("SELECT saleID FROM sales where saleID = :randomID LIMIT 1", {'randomID':saleID})
            if c.fetchone():
                y = TRUE
            else:
                y = FALSE
        #Seeing if extra service box checked   
        if self.startMonth.get() != self.endMonth.get():
            if self.startMonth.get()== 1 or 3 or 5 or 7 or 8 or 10 or 12:
                duration = 31 -self.startDay.get() + self.endDate.get()
            elif self.startMonth.get()== 4 or 6 or 9 or 11:
                duration = 30 -self.startDay.get() + self.endDate.get()
            elif self.startMonth.get()== 2:
                if calendar.isleap(self.startYear.get()) == True:
                    duration = 29-self.startDay.get() + self.endDate.get()
                else:
                    duration = 28-self.startDay.get() + self.endDate.get()
        else:
            duration = self.endDate.get() - self.startDate.get() 
         
        cost = 50.00*duration     
        extraServ = linensTrue.get()
        if extraServ == 0:
            extraPrice = '$0.00'
            services = 'No'
        else:
            extraPrice = '$15.00'
            services = 'Yes'
            cost += 15.00
        
        c.execute("INSERT INTO sales VALUES (:salesId, :customerId, :resDate, :extraServices, :extraCost, :totalCost)",
                  {'salesId':saleID,
                   'customerId':custID,
                   'resDate':self.startDate.get(),
                   'extraServices':services,
                   'extraCost':extraPrice,
                   'totalCost':cost
                   })
        
        conn.commit()    
        conn.close()
  
#  -- main  --

root = tk.Tk()
root.title("Request Reservation")
root.geometry("500x500")
ReservationFrame(root)
root.mainloop()
