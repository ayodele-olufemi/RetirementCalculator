# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:43:13 2020

@author: ayyor
"""

import tkinter as tk
import tkinter.ttk as tkk
import datetime
import matplotlib.pyplot as plt


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



numOfConfigurations = 1

HEIGHT = 1080
WIDTH = 1920

app = tk.Tk()
app.title("IT680 - Retirement Calculator")
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH, bg="#aecad0")
canvas.pack()


nav = tk.Frame(canvas, bg="#000000")
nav.place(relwidth=1, relheight=0.1)


appName = tk.Label(nav, text="Retirement Calculator", font=("Helvetica 26 bold italic"), fg="#ff9933", bg="#000000")  
appName.pack(expand=True)


form = tk.Frame(canvas, bg="#263D42")
form.place(relx=0, rely=0.105, relwidth=0.5, relheight=0.9)





















tableFrame = tk.Frame(canvas, bg="#262122")
tableFrame.place(relx=0.5, rely=0.105, relwidth=0.5, relheight=0.9)











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


L_averageAnnualSalaryIncrease = tk.Label(formLabelsFrame, text="Annual Salary Increase(%): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_averageAnnualSalaryIncrease.place(relx=0.005, rely=0.38)


L_desiredEstate = tk.Label(formLabelsFrame, text="Desired Estate Amount: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_desiredEstate.place(relx=0.005, rely=0.41)


L_confName = tk.Label(formLabelsFrame, text="Configuration Name: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_confName.place(relx=0.005, rely=0.44)






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


E_averageAnnualSalaryIncrease = tk.Entry(formEntryFrame, bg="white")
E_averageAnnualSalaryIncrease.place(relx=0, rely=0.38, relwidth=1)
E_averageAnnualSalaryIncrease_ttp = CreateToolTip(E_averageAnnualSalaryIncrease, "Enter estimated average annual salary increase")


E_desiredEstate = tk.Entry(formEntryFrame, bg="white")
E_desiredEstate.place(relx=0, rely=0.41, relwidth=1)
E_desiredEstate_ttp = CreateToolTip(E_desiredEstate, "If desired, enter estimated amount you'd like to leave to your heirs")


E_confName = tk.Entry(formEntryFrame, bg="white")
E_confName.place(relx=0, rely=0.44, relwidth=1)
E_confName_ttp = CreateToolTip(E_confName, "Enter a name for this configuration")


E_comparison = tk.Button(formEntryFrame, text="Add Another Configuration?", command=lambda: compareControl())
E_comparison.place(relx=0, rely=0.47, relwidth=1)


def compareControl():
    global numOfConfigurations
    numOfConfigurations = 2
    E_fName2.place(relx=0, rely=0, relwidth=1)
    E_lName2.place(relx=0, rely=0.03, relwidth=1)
    E_Email2.place(relx=0, rely=0.06, relwidth=1)
    
    E_fName2.insert('end', E_fName.get())
    E_lName2.insert('end', E_lName.get())
    E_Email2.insert('end', E_Email.get())
    
    E_currentAge2.place(relx=0, rely=0.09, relwidth=1)
    E_retireAge2.place(relx=0, rely=0.12, relwidth=1)
    E_lifeExpectancy2.place(relx=0, rely=0.15, relwidth=1)
    E_currentAnnualSalary2.place(relx=0, rely=0.18, relwidth=1)
    S_annualRetCont2.place(relx=0, rely=0.21, relwidth=1)
    E_currentRetSavings2.place(relx=0, rely=0.26, relwidth=1)
    E_desAnnualRetIncomeA2.place(relx=0, rely=0.29, relwidth=1)
    E_desAnnualRetIncomeI2.place(relx=0, rely=0.32, relwidth=1)
    E_averageAnnualReturnRate2.place(relx=0, rely=0.35, relwidth=1)
    E_averageAnnualSalaryIncrease2.place(relx=0, rely=0.38, relwidth=1)
    E_desiredEstate2.place(relx=0, rely=0.41, relwidth=1)
    E_confName2.place(relx=0, rely=0.44, relwidth=1)
    E_comparison2.place(relx=0, rely=0.47, relwidth=1)
    E_comparison.place_forget()



#form2 entry frame
formEntryFrame2 = tk.Frame(form, bg="#263D42")
formEntryFrame2.place(relx=0.5, rely=0.03, relwidth=0.2, relheight=1)

#entries in formEntry
E_fName2 = tk.Entry(formEntryFrame2, bg="white")
E_fName2_ttp = CreateToolTip(E_fName2, "Enter first name")


E_lName2 = tk.Entry(formEntryFrame2, bg="white")
E_lName2_ttp = CreateToolTip(E_lName2, "Enter last name")


E_Email2 = tk.Entry(formEntryFrame2, bg="white")
E_Email2_ttp = CreateToolTip(E_Email2, "Enter your email address")


E_currentAge2 = tk.Entry(formEntryFrame2, bg="white")
E_currentAge2_ttp = CreateToolTip(E_currentAge2, "Enter age at the end of current year")


E_retireAge2 = tk.Entry(formEntryFrame2, bg="white")
E_retireAge2_ttp = CreateToolTip(E_retireAge2, "Enter age you plan to retire at")


E_lifeExpectancy2 = tk.Entry(formEntryFrame2, bg="white")
E_lifeExpectancy2_ttp = CreateToolTip(E_lifeExpectancy2, "Enter age you expect to live to")


E_currentAnnualSalary2 = tk.Entry(formEntryFrame2, bg="white")
E_currentAnnualSalary2_ttp = CreateToolTip(E_currentAnnualSalary2, "Enter your current annual salary")


S_annualRetCont2 = tk.Scale(formEntryFrame2, from_=0, to=100, orient='horizontal')
S_annualRetCont2_ttp = CreateToolTip(S_annualRetCont2, "Slide as percentage of annual salary")


E_currentRetSavings2 = tk.Entry(formEntryFrame2, bg="white")
E_currentRetSavings2_ttp = CreateToolTip(E_currentRetSavings2, "Enter your current total savings towards retirement")


E_desAnnualRetIncomeA2 = tk.Entry(formEntryFrame2, bg="white")
E_desAnnualRetIncomeA2_ttp = CreateToolTip(E_desAnnualRetIncomeA2, "Enter your desired annual retimrement income during active years i.e. till age 80 years")


E_desAnnualRetIncomeI2 = tk.Entry(formEntryFrame2, bg="white")
E_desAnnualRetIncomeI2_ttp = CreateToolTip(E_desAnnualRetIncomeI2, "Enter your desired annual retimrement income after active years i.e. after age 80 years")


E_averageAnnualReturnRate2 = tk.Entry(formEntryFrame2, bg="white")
E_averageAnnualReturnRate2_ttp = CreateToolTip(E_averageAnnualReturnRate2, "Enter estimated average annual return rate")


E_averageAnnualSalaryIncrease2 = tk.Entry(formEntryFrame2, bg="white")
E_averageAnnualSalaryIncrease2_ttp = CreateToolTip(E_averageAnnualSalaryIncrease2, "Enter estimated average annual salary increase")


E_desiredEstate2 = tk.Entry(formEntryFrame2, bg="white")
E_desiredEstate2_ttp = CreateToolTip(E_desiredEstate2, "If desired, enter estimated amount you'd like to leave to your heirs")


E_confName2 = tk.Entry(formEntryFrame2, bg="white")
E_confName2_ttp = CreateToolTip(E_confName2, "Enter a name for this configuration")

E_comparison2 = tk.Button(formEntryFrame2, text="Add Another Configuration?", command=lambda: compareControl2())


def compareControl2():
    global numOfConfigurations
    numOfConfigurations = 3
    E_fName3.place(relx=0, rely=0, relwidth=1)
    E_lName3.place(relx=0, rely=0.03, relwidth=1)
    E_Email3.place(relx=0, rely=0.06, relwidth=1)
    
    E_fName3.insert('end', E_fName.get())
    E_lName3.insert('end', E_lName.get())
    E_Email3.insert('end', E_Email.get())
    
    E_currentAge3.place(relx=0, rely=0.09, relwidth=1)
    E_retireAge3.place(relx=0, rely=0.12, relwidth=1)
    E_lifeExpectancy3.place(relx=0, rely=0.15, relwidth=1)
    E_currentAnnualSalary3.place(relx=0, rely=0.18, relwidth=1)
    S_annualRetCont3.place(relx=0, rely=0.21, relwidth=1)
    E_currentRetSavings3.place(relx=0, rely=0.26, relwidth=1)
    E_desAnnualRetIncomeA3.place(relx=0, rely=0.29, relwidth=1)
    E_desAnnualRetIncomeI3.place(relx=0, rely=0.32, relwidth=1)
    E_averageAnnualReturnRate3.place(relx=0, rely=0.35, relwidth=1)
    E_averageAnnualSalaryIncrease3.place(relx=0, rely=0.38, relwidth=1)
    E_desiredEstate3.place(relx=0, rely=0.41, relwidth=1)
    E_confName3.place(relx=0, rely=0.44, relwidth=1)
    E_comparison2.place_forget()





#form3 entry frame
formEntryFrame3 = tk.Frame(form, bg="#263D42")
formEntryFrame3.place(relx=0.735, rely=0.03, relwidth=0.2, relheight=1)

#entries in formEntry
E_fName3 = tk.Entry(formEntryFrame3, bg="white")
E_fName3_ttp = CreateToolTip(E_fName3, "Enter first name")


E_lName3 = tk.Entry(formEntryFrame3, bg="white")
E_lName3_ttp = CreateToolTip(E_lName3, "Enter last name")


E_Email3 = tk.Entry(formEntryFrame3, bg="white")
E_Email3_ttp = CreateToolTip(E_Email3, "Enter your email address")


E_currentAge3 = tk.Entry(formEntryFrame3, bg="white")
E_currentAge3_ttp = CreateToolTip(E_currentAge3, "Enter age at the end of current year")


E_retireAge3 = tk.Entry(formEntryFrame3, bg="white")
E_retireAge3_ttp = CreateToolTip(E_retireAge3, "Enter age you plan to retire at")


E_lifeExpectancy3 = tk.Entry(formEntryFrame3, bg="white")
E_lifeExpectancy3_ttp = CreateToolTip(E_lifeExpectancy3, "Enter age you expect to live to")


E_currentAnnualSalary3 = tk.Entry(formEntryFrame3, bg="white")
E_currentAnnualSalary3_ttp = CreateToolTip(E_currentAnnualSalary3, "Enter your current annual salary")


S_annualRetCont3 = tk.Scale(formEntryFrame3, from_=0, to=100, orient='horizontal')
S_annualRetCont3_ttp = CreateToolTip(S_annualRetCont3, "Slide as percentage of annual salary")


E_currentRetSavings3 = tk.Entry(formEntryFrame3, bg="white")
E_currentRetSavings3_ttp = CreateToolTip(E_currentRetSavings3, "Enter your current total savings towards retirement")


E_desAnnualRetIncomeA3 = tk.Entry(formEntryFrame3, bg="white")
E_desAnnualRetIncomeA3_ttp = CreateToolTip(E_desAnnualRetIncomeA3, "Enter your desired annual retimrement income during active years i.e. till age 80 years")


E_desAnnualRetIncomeI3 = tk.Entry(formEntryFrame3, bg="white")
E_desAnnualRetIncomeI3_ttp = CreateToolTip(E_desAnnualRetIncomeI3, "Enter your desired annual retimrement income after active years i.e. after age 80 years")


E_averageAnnualReturnRate3 = tk.Entry(formEntryFrame3, bg="white")
E_averageAnnualReturnRate3_ttp = CreateToolTip(E_averageAnnualReturnRate3, "Enter estimated average annual return rate")


E_averageAnnualSalaryIncrease3 = tk.Entry(formEntryFrame3, bg="white")
E_averageAnnualSalaryIncrease3_ttp = CreateToolTip(E_averageAnnualSalaryIncrease3, "Enter estimated average annual salary increase")


E_desiredEstate3 = tk.Entry(formEntryFrame3, bg="white")
E_desiredEstate3_ttp = CreateToolTip(E_desiredEstate3, "If desired, enter estimated amount you'd like to leave to your heirs")


E_confName3 = tk.Entry(formEntryFrame3, bg="white")
E_confName3_ttp = CreateToolTip(E_confName3, "Enter a name for this configuration")



B_calculateButton = tk.Button(form, text="Calculate", command=lambda: calculateRetirement())
B_calculateButton.place(relx=0.11, rely=0.55, relwidth=0.1)

B_resetButton = tk.Button(form, text="Reset", command=lambda: clearAll())
B_resetButton.place(relx=0.26, rely=0.55, relwidth=0.1)



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
    E_averageAnnualSalaryIncrease.insert('end', "2")
    E_desiredEstate.insert('end', "100000")
    
def calculateRetirement():
    try:
        rMDAge = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]
        rMD70 = [27.4, 26.5, 25.6, 24.7, 23.8, 22.9, 22, 21.2, 20.3, 19.5, 18.7, 17.9, 17.1, 16.3, 15.5, 14.8, 14.1, 13.4, 12.7, 12, 11.4, 10.8, 10, 2, 9.6, 9.1, 8.6, 8.1, 7.6, 7.1, 6.7, 6.3, 5.9, 5.5, 5.2, 4.9, 4.5, 4.2, 3.9, 3.7, 3.4, 3.1, 2.9, 2.4, 2.1, 1.9]
        ssnBenStartAge = [62,63,64,65,66,67,68,69,70,71,72,73,74,75]
        ssnBenefit62 = [16000,16500,17000,17500,18000,18500,19000,19500,20000,20500,21000,21500,22000,22500]
        
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
        avgAnnualSalaryIncrease = float(E_averageAnnualSalaryIncrease.get())
        desiredEstate = float(E_desiredEstate.get())
        configurationName = E_confName.get()
        currentYear = datetime.datetime.now().year
        retirementTable = []
        tableRows = range(currentAge + 1, 101)
        
        if retireAge < 62:
            ssnAmount = 0
        else:
            ssnAmount = round(ssnBenefit62[ssnBenStartAge.index(retireAge)])
        
        firstRow = []
        firstRow.append("Year")                     #0
        firstRow.append("Age")                      #1
        firstRow.append("Annual Sal")               #2
        firstRow.append("Annual Sav")               #3
        firstRow.append("Growth")                   #4
        firstRow.append("Soc Sec")          #5
        firstRow.append("RMD")                      #6
        firstRow.append("Desired Sal")              #7
        firstRow.append("Withdrawn")                #8
        firstRow.append("Nest Egg")                 #9
        
        secondRow = []
        secondRow.append(currentYear)
        currentYear = currentYear + 1
        secondRow.append(currentAge)
        secondRow.append(round(curAnnualSalary))
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(0)
        secondRow.append(round(curRetirmentSavings))
        
        retirementTable.append(firstRow)
        retirementTable.append(secondRow)
        
        
        for x in tableRows: 
            thisRow = []
            #append Year
            thisRow.append(currentYear)
            currentYear = currentYear + 1
            
            #append Age
            thisRow.append(x)
            
            if x < retireAge:
                #increase salary and append it
                curAnnualSalary = curAnnualSalary + (curAnnualSalary * (avgAnnualSalaryIncrease / 100.0))
                thisRow.append(round(curAnnualSalary))
                
                #calculate retirement contribution savings and append it
                thisRow.append(round(thisRow[2] * (curAnnualContPercent / 100.0)))
                
                #calculate returns and append it
                growth = (avgAnnualReturnRate / 100.0) * curRetirmentSavings
                thisRow.append(round(growth))
                
                #append zero for [5] - [8]
                thisRow.append(0)
                thisRow.append(0)
                thisRow.append(0)
                thisRow.append(0)
                
                #calculate new nest egg and append it
                curRetirmentSavings = curRetirmentSavings + thisRow[3] + thisRow[4]
                thisRow.append(round(curRetirmentSavings))
            else:
                #append zero for salary and savings
                thisRow.append(0)
                thisRow.append(0)
                
                #calculate and append returns
                growth = (avgAnnualReturnRate / 100.0) * curRetirmentSavings
                thisRow.append(round(growth))
                
                if x < 62:
                    #append zero for [5] - [8]
                    thisRow.append(0)
                    thisRow.append(0)
                    thisRow.append(0)
                    thisRow.append(0)
                else:
                    thisRow.append(ssnAmount)
                    if x < 70:
                        thisRow.append(0)
                    else:
                        rmdFactor = rMD70[rMDAge.index(x)]
                        rmdValue = curRetirmentSavings / rmdFactor
                        thisRow.append(round(rmdValue))
                    thisRow.append(round(darIncomeActive))
                    if thisRow[7] < thisRow[6]:
                        thisRow.append(thisRow[6] - thisRow[5])
                    else: 
                        thisRow.append(thisRow[7] - thisRow[5])
                curRetirmentSavings = curRetirmentSavings + thisRow[3] + thisRow[4] - thisRow[8]
                thisRow.append(round(curRetirmentSavings))
                
            retirementTable.append(thisRow)
            
            if curRetirmentSavings < 0:
                break
        
        finalAge = retirementTable[len(retirementTable)-1][1]
        #try output
        for y in retirementTable:
            print(y[0], "{0:>5}".format(y[1]), "{0:>10}".format(y[2]), "{0:>10}".format(y[3]), "{0:>10}".format(y[4]), "{0:>10}".format(y[5]), "{0:>10}".format(y[6]), "{0:>10}".format(y[7]), "{0:>10}".format(y[8]), "{0:>10}".format(y[9]))
        
        
        #extract Nest Egg
        nestEgg = []
        for k in retirementTable:
            nestEgg.append(k[9])
        plt.plot(range(currentAge, finalAge + 1), nestEgg[1:])
        
        
        
        if numOfConfigurations == 1:
            tablayout = tkk.Notebook(tableFrame)
            tab1 = tk.Frame(tablayout)
            tab1.pack(fill="both")
            
            
            
            sb = tk.Scrollbar(tab1)  
            sb.pack(side = tk.RIGHT, fill = tk.Y)
            mylist1 = tk.Listbox(tab1, height=1, width=154, font=("Helvetica 11 bold"))  
              
            for line in range(1,2):  
                mylist1.insert(tk.END, "{:1}{:^10}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}{:^15}{:1}".format("|",retirementTable[0][0],"|",retirementTable[0][1],"|",retirementTable[0][2],"|",retirementTable[0][3],"|",retirementTable[0][4],"|",retirementTable[0][5],"|",retirementTable[0][6],"|",retirementTable[0][7],"|",retirementTable[0][8],"|",retirementTable[0][9],"|"))  
              
            mylist1.pack( side = tk.TOP )  
              
            
            
            mylist = tk.Listbox(tab1, height=55, width=154, font=("Helvetica 11"), yscrollcommand = sb.set )  
              
            for line in retirementTable[1:]:  
                mylist.insert(tk.END, "{:1}{:>10}{:1}{:>15}{:1}{:>15}{:1}{:<15}{:1}{:<15}{:1}{:<15}{:1}{:<15}{:1}{:<15}{:1}{:<15}{:1}{:<15}{:1}".format("|",line[0],"|",line[1],"|",line[2],"|",line[3],"|",line[4],"|",line[5],"|",line[6],"|",line[7],"|",line[8],"|",line[9],"|"))  
              
            mylist.pack( side = tk.LEFT )  
            sb.config( command = mylist.yview ) 
            
            tablayout.add(tab1,text=configurationName)
            #tablayout.pack(fill="both")
            tablayout.place(relx=0.005, rely=0, relwidth=0.99)
            
            
        if numOfConfigurations == 2: 
            tablayout = tkk.Notebook(tableFrame)
            tab1 = tk.Frame(tablayout)
            tab1.pack(fill="both")
            
            for row in range(5):
                for column in range(6):
                    if row==0:
                        label = tk.Entry(tab1, text="Heading : " + str(column))
                        label.config(font=('Arial',14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    else:
                        label=tk.Entry(tab1,text="Row : "+str(row)+" , Column : "+str(column))
                        label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                        tab1.grid_columnconfigure(column,weight=1)
            
            tablayout.add(tab1,text="TAB 1")
            
            
            #tab2
            tab2=tk.Frame(tablayout)
            tab2.pack(fill="both")
            
            #adding table into tab
            
            for row in range(5):
                for column in range(6):
                    if row==0:
                        label = tk.Label(tab2, text="Heading : " + str(column), bg="white", fg="black", padx=3,
                                      pady=3)
                        label.config(font=('Arial',14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        tab2.grid_columnconfigure(column, weight=1)
                    else:
                        label=tk.Label(tab2,text="Row : "+str(row)+" , Column : "+str(column),bg="black",fg="white",padx=3,pady=3)
                        label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                        tab2.grid_columnconfigure(column,weight=1)
            
            tablayout.add(tab2,text="TAB 2")
            
            #tablayout.pack(fill="both")
            tablayout.place(relx=0.05, rely=0, relwidth=0.9)
            
        if numOfConfigurations == 3:
            tablayout = tkk.Notebook(tableFrame)
            tab1 = tk.Frame(tablayout)
            tab1.pack(fill="both")
            
            for row in range(5):
                for column in range(6):
                    if row==0:
                        label = tk.Entry(tab1, text="Heading : " + str(column))
                        label.config(font=('Arial',14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    else:
                        label=tk.Entry(tab1,text="Row : "+str(row)+" , Column : "+str(column))
                        label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                        tab1.grid_columnconfigure(column,weight=1)
            
            tablayout.add(tab1,text="TAB 1")
            
            
            #tab2
            tab2=tk.Frame(tablayout)
            tab2.pack(fill="both")
            
            #adding table into tab
            
            for row in range(5):
                for column in range(6):
                    if row==0:
                        label = tk.Label(tab2, text="Heading : " + str(column), bg="white", fg="black", padx=3,
                                      pady=3)
                        label.config(font=('Arial',14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        tab2.grid_columnconfigure(column, weight=1)
                    else:
                        label=tk.Label(tab2,text="Row : "+str(row)+" , Column : "+str(column),bg="black",fg="white",padx=3,pady=3)
                        label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                        tab2.grid_columnconfigure(column,weight=1)
            
            tablayout.add(tab2,text="TAB 2")
            
            
            #tab3
            tab3=tk.Frame(tablayout)
            tab3.pack(fill="both")
            
            #adding table into tab
            
            for row in range(5):
                for column in range(6):
                    if row==0:
                        label = tk.Label(tab3, text="Heading : " + str(column), bg="white", fg="black", padx=3,
                                      pady=3)
                        label.config(font=('Arial',14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        tab3.grid_columnconfigure(column, weight=1)
                    else:
                        label=tk.Label(tab3,text="Row : "+str(row)+" , Column : "+str(column),bg="black",fg="white",padx=3,pady=3)
                        label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                        tab3.grid_columnconfigure(column,weight=1)
            
            tablayout.add(tab3,text="TAB 3")
            
            #tablayout.pack(fill="both")
            tablayout.place(relx=0.05, rely=0, relwidth=0.9)
        
        
        

    except: 
        print("there is an error in your inputs")
    

app.mainloop()
