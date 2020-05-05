'''
Created on May 5, 2020

@author: alita
'''
import databaseModule

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
        
    print("Start Date", self.startDate.get())
    self.startDate.set("")
        
    print("End Date", self.endDate.get())
    self.endDate.set("")
        
        
def save(self):    
        #databaseModule.main()    
        
        #custFirst = self.customerFirstName.get()
        #custLast = self.customerLastName.get()
        #custCity = self.customerCity.get()
        
        #sql = """INSERT INTO customer 
        #            (custFirst, custLast, custCity) 
        #        VALUES (?, ?, ?)"""
        #c.execute(sql, (custFirst, custLast, custCity))
        #conn.commit()    
        #print("Saved")
        
def exit(self):
        root.destroy()   
