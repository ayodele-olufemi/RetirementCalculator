# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:43:13 2020

@author: ayyor
"""

import tkinter as tk
import datetime


class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='yellow', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()








HEIGHT = 1080
WIDTH = 1920

app = tk.Tk()
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH, bg="#aecad0")
canvas.pack()


nav = tk.Frame(canvas, bg="#000000")
nav.place(relwidth=1, relheight=0.1)


appName = tk.Label(nav, text="Retirement Calculator", font=("Helvetica 26 bold italic"), fg="#ff9933", bg="#000000")  
appName.pack(expand=True)


form = tk.Frame(canvas, bg="#263D42")
form.place(relx=0.005, rely=0.105, relwidth=0.5, relheight=0.9)


formName = tk.Label(form, text="Retirement Form", font=("Helvetica 16 bold "), fg="yellow", bg="#263D42")  
formName.place(relx=0.14, rely=0)

#form labels frame
formLabelsFrame = tk.Frame(form, bg="#263D42")
formLabelsFrame.place(relx=0.005, rely=0.03, relwidth=0.25, relheight=1)

#labels in formLabel
L_fName = tk.Label(formLabelsFrame, text="First Name: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_fName.place(relx=0.005, rely=0)


L_lName = tk.Label(formLabelsFrame, text="Last Name: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_lName.place(relx=0.005, rely=0.03)


L_Email = tk.Label(formLabelsFrame, text="Email: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_Email.place(relx=0.005, rely=0.06)


L_currentAge = tk.Label(formLabelsFrame, text="Current Age: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentAge.place(relx=0.005, rely=0.09)


L_retireAge = tk.Label(formLabelsFrame, text="Planned Retirement Age: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_retireAge.place(relx=0.005, rely=0.12)


L_lifeExpectancy = tk.Label(formLabelsFrame, text="Life Expectancy: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_lifeExpectancy.place(relx=0.005, rely=0.15)


L_currentAnnualSalary = tk.Label(formLabelsFrame, text="Current Annual Salary: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentAnnualSalary.place(relx=0.005, rely=0.18)


L_annualRetCont = tk.Label(formLabelsFrame, text="Annual Retirement Contribution (%): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_annualRetCont.place(relx=0.005, rely=0.23)


L_currentRetSavings = tk.Label(formLabelsFrame, text="Current Total Retirement Savings: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentRetSavings.place(relx=0.005, rely=0.26)


L_desAnnualRetIncomeA = tk.Label(formLabelsFrame, text="DAR Income (Active Years): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_desAnnualRetIncomeA.place(relx=0.005, rely=0.29)

L_desAnnualRetIncomeI = tk.Label(formLabelsFrame, text="DAR Income (Inactive Years): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_desAnnualRetIncomeI.place(relx=0.005, rely=0.32)


L_averageAnnualReturnRate = tk.Label(formLabelsFrame, text="Average Annual Return Rate (%): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_averageAnnualReturnRate.place(relx=0.005, rely=0.35)


L_comparison = tk.Checkbutton(formLabelsFrame, text="Compare with two other plans?")
L_comparison.place(relx=0.005, rely=0.38)













#form entry frame
formEntryFrame = tk.Frame(form, bg="#263D42")
formEntryFrame.place(relx=0.265, rely=0.03, relwidth=0.2, relheight=1)

#entries in formEntry
E_fName = tk.Entry(formEntryFrame, bg="white")
E_fName.place(relx=0, rely=0, relwidth=1)
E_fName_ttp = CreateToolTip(E_fName, "Enter first name")


E_lName = tk.Entry(formEntryFrame, bg="white")
E_lName.place(relx=0, rely=0.03, relwidth=1)
E_lName_ttp = CreateToolTip(E_lName, "Enter last name")


E_Email = tk.Entry(formEntryFrame, bg="white")
E_Email.place(relx=0, rely=0.06, relwidth=1)
E_Email_ttp = CreateToolTip(E_Email, "Enter your email address")


E_currentAge = tk.Entry(formEntryFrame, bg="white")
E_currentAge.place(relx=0, rely=0.09, relwidth=1)
E_currentAge_ttp = CreateToolTip(E_currentAge, "Enter age at the end of current year")


E_retireAge = tk.Entry(formEntryFrame, bg="white")
E_retireAge.place(relx=0, rely=0.12, relwidth=1)
E_retireAge_ttp = CreateToolTip(E_retireAge, "Enter age you plan to retire at")


E_lifeExpectancy = tk.Entry(formEntryFrame, bg="white")
E_lifeExpectancy.place(relx=0, rely=0.15, relwidth=1)
E_lifeExpectancy_ttp = CreateToolTip(E_lifeExpectancy, "Enter age you expect to live to")


E_currentAnnualSalary = tk.Entry(formEntryFrame, bg="white")
E_currentAnnualSalary.place(relx=0, rely=0.18, relwidth=1)
E_currentAnnualSalary_ttp = CreateToolTip(E_currentAnnualSalary, "Enter your current annual salary")


S_annualRetCont = tk.Scale(formEntryFrame, from_=0, to=100, orient='horizontal')
S_annualRetCont.place(relx=0, rely=0.21, relwidth=1)
S_annualRetCont_ttp = CreateToolTip(S_annualRetCont, "Slide as percentage of annual salary")


E_currentRetSavings = tk.Entry(formEntryFrame, bg="white")
E_currentRetSavings.place(relx=0, rely=0.26, relwidth=1)
E_currentRetSavings_ttp = CreateToolTip(E_currentRetSavings, "Enter your current total savings towards retirement")


E_desAnnualRetIncomeA = tk.Entry(formEntryFrame, bg="white")
E_desAnnualRetIncomeA.place(relx=0, rely=0.29, relwidth=1)
E_desAnnualRetIncomeA_ttp = CreateToolTip(E_desAnnualRetIncomeA, "Enter your desired annual retimrement income during active years i.e. till age 80 years")


E_desAnnualRetIncomeI = tk.Entry(formEntryFrame, bg="white")
E_desAnnualRetIncomeI.place(relx=0, rely=0.32, relwidth=1)
E_desAnnualRetIncomeI_ttp = CreateToolTip(E_desAnnualRetIncomeI, "Enter your desired annual retimrement income after active years i.e. after age 80 years")


E_averageAnnualReturnRate = tk.Entry(formEntryFrame, bg="white")
E_averageAnnualReturnRate.place(relx=0, rely=0.35, relwidth=1)
E_averageAnnualReturnRate_ttp = CreateToolTip(E_averageAnnualReturnRate, "Enter estimated average annual return rate")


B_calculateButton = tk.Button(form, text="Calculate", command=lambda: calculateRetirement())
B_calculateButton.place(relx=0.11, rely=0.46, relwidth=0.1)

B_resetButton = tk.Button(form, text="Reset", command=lambda: clearAll())
B_resetButton.place(relx=0.26, rely=0.46, relwidth=0.1)



#defining the reset button
def clearAll2():
    E_fName.delete(0, 'end')
    E_lName.delete(0, 'end')
    E_Email.delete(0, 'end')
    E_currentAge.delete(0, 'end')
    E_retireAge.delete(0, 'end')
    E_lifeExpectancy.delete(0, 'end')
    E_currentAnnualSalary.delete(0, 'end')
    S_annualRetCont.set(0)
    E_currentRetSavings.delete(0, 'end')
    E_desAnnualRetIncomeA.delete(0, 'end')
    E_desAnnualRetIncomeI.delete(0, 'end')
    L_averageAnnualReturnRate.delete(0, 'end')

def clearAll():
    E_fName.insert('end', "Ayodele")
    E_lName.insert('end', "Olufemi")
    E_Email.insert('end', "ayodele.olufemi@mnsu.edu")
    E_currentAge.insert('end', "45")
    E_retireAge.insert('end', "67")
    E_lifeExpectancy.insert('end', "100")
    E_currentAnnualSalary.insert('end', "50000")
    S_annualRetCont.set(8)
    E_currentRetSavings.insert('end', "100000")
    E_desAnnualRetIncomeA.insert('end', "45000")
    E_desAnnualRetIncomeI.insert('end', "20000")
    E_averageAnnualReturnRate.insert('end', "4")
    
def calculateRetirement():
    try: 
        firstName = E_fName.get()
        lastName = E_lName.get()
        email = E_Email.get()
        currentAge = int(E_currentAge.get())
        retireAge = int(E_retireAge.get())
        lifeExpectancy = E_lifeExpectancy.get()
        curAnnualSalary = float(E_currentAnnualSalary.get())
        curAnnualContPercent =  int(S_annualRetCont.get())
        curRetirmentSavings = float(E_currentRetSavings.get())
        darIncomeActive = float(E_desAnnualRetIncomeA.get())
        darIncomeInactive = float(E_desAnnualRetIncomeI.get())
        avgAnnualReturnRate = float(E_averageAnnualReturnRate.get())
        currentYear = datetime.datetime.now().year
        retirementTable = []
        tableRows = range(currentAge + 1, 101)
        numberOfRows = len(tableRows)
        
        firstRow = []
        firstRow.append("Year")
        firstRow.append("Age")
        firstRow.append("Annual Sal")
        firstRow.append("Annual Sav")
        firstRow.append("Growth")
        firstRow.append("Withdrawal")
        firstRow.append("Nest Egg")
        
        secondRow = []
        secondRow.append(currentYear)
        currentYear = currentYear + 1
        secondRow.append(currentAge)
        secondRow.append(round(curAnnualSalary))
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(round(curRetirmentSavings))
        
        retirementTable.append(firstRow)
        retirementTable.append(secondRow)
        
        
        for x in tableRows: 
            thisRow = []
            
            thisRow.append(currentYear)
            currentYear = currentYear + 1
            
            thisRow.append(x)
            
            if x < retireAge:
                thisRow.append(round(curAnnualSalary))
                thisRow.append(round(thisRow[2] * (curAnnualContPercent / 100.0)))
                growth = (avgAnnualReturnRate / 100.0) * curRetirmentSavings
                thisRow.append(round(growth))
                thisRow.append(0)
                curRetirmentSavings = curRetirmentSavings + thisRow[3] + thisRow[4] - thisRow[5]
                thisRow.append(round(curRetirmentSavings))
            else:
                thisRow.append(0)
                thisRow.append(0)
                growth = (avgAnnualReturnRate / 100.0) * curRetirmentSavings
                thisRow.append(round(growth))
                thisRow.append(round(darIncomeActive))
                curRetirmentSavings = curRetirmentSavings + thisRow[3] + thisRow[4] - thisRow[5]
                thisRow.append(round(curRetirmentSavings))
                
            retirementTable.append(thisRow)
        
        
        #try output
        for y in retirementTable:
            print(y[0], "{0:>5}".format(y[1]), "{0:>10}".format(y[2]), "{0:>10}".format(y[3]), "{0:>10}".format(y[4]), "{0:>10}".format(y[5]), "{0:>10}".format(y[6]))
        
        
        
        
    except: 
        print("there is an error in your inputs")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

app.mainloop()