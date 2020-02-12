# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:43:13 2020

@author: ayyor
"""

import tkinter as tk


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


L_currentAge = tk.Label(formLabelsFrame, text="Current Age: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentAge.place(relx=0.005, rely=0.06)


L_retireAge = tk.Label(formLabelsFrame, text="Planned Retirement Age: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_retireAge.place(relx=0.005, rely=0.09)


L_lifeExpectancy = tk.Label(formLabelsFrame, text="Life Expectancy: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_lifeExpectancy.place(relx=0.005, rely=0.12)


L_currentAnnualSalary = tk.Label(formLabelsFrame, text="Current Annual Salary: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentAnnualSalary.place(relx=0.005, rely=0.15)


L_annualRetCont = tk.Label(formLabelsFrame, text="Annual Retirement Contribution (%): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_annualRetCont.place(relx=0.005, rely=0.18)


L_currentRetSavings = tk.Label(formLabelsFrame, text="Current Total Retirement Savings: ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_currentRetSavings.place(relx=0.005, rely=0.23)


L_desAnnualRetIncomeA = tk.Label(formLabelsFrame, text="DAR Income (Active Years): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_desAnnualRetIncomeA.place(relx=0.005, rely=0.26)

L_desAnnualRetIncomeI = tk.Label(formLabelsFrame, text="DAR Income (Inactive Years): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_desAnnualRetIncomeI.place(relx=0.005, rely=0.29)


L_averageAnnualReturnRate = tk.Label(formLabelsFrame, text="Average Annual Return Rate (%): ", fg="white", font=("Helvetica 10 bold"), bg="#263D42")
L_averageAnnualReturnRate.place(relx=0.005, rely=0.32)


L_comparison = tk.Checkbutton(formLabelsFrame, text="Compare with two other plans?")
L_comparison.place(relx=0.005, rely=0.36)













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


E_currentAge = tk.Entry(formEntryFrame, bg="white")
E_currentAge.place(relx=0, rely=0.06, relwidth=1)
E_currentAge_ttp = CreateToolTip(E_currentAge, "Enter age at the end of current year")


E_retireAge = tk.Entry(formEntryFrame, bg="white")
E_retireAge.place(relx=0, rely=0.09, relwidth=1)
E_retireAge_ttp = CreateToolTip(E_retireAge, "Enter age you plan to retire at")


E_lifeExpectancy = tk.Entry(formEntryFrame, bg="white")
E_lifeExpectancy.place(relx=0, rely=0.12, relwidth=1)
E_retireAge_ttp = CreateToolTip(E_lifeExpectancy, "Enter age you expect to live to")


E_currentAnnualSalary = tk.Entry(formEntryFrame, bg="white")
E_currentAnnualSalary.place(relx=0, rely=0.15, relwidth=1)
E_currentAnnualSalary_ttp = CreateToolTip(E_currentAnnualSalary, "Enter your current annual salary")


S_annualRetCont = tk.Scale(formEntryFrame, from_=0, to=100, orient='horizontal')
S_annualRetCont.place(relx=0, rely=0.18, relwidth=1)
S_annualRetCont_ttp = CreateToolTip(S_annualRetCont, "Slide as percentage of annual salary")


E_currentRetSavings = tk.Entry(formEntryFrame, bg="white")
E_currentRetSavings.place(relx=0, rely=0.23, relwidth=1)
E_currentRetSavings_ttp = CreateToolTip(E_currentRetSavings, "Enter your current total savings towards retirement")


E_desAnnualRetIncomeA = tk.Entry(formEntryFrame, bg="white")
E_desAnnualRetIncomeA.place(relx=0, rely=0.26, relwidth=1)
E_desAnnualRetIncomeA_ttp = CreateToolTip(E_desAnnualRetIncomeA, "Enter your desired annual retimrement income during active years i.e. till age 80 years")


E_desAnnualRetIncomeI = tk.Entry(formEntryFrame, bg="white")
E_desAnnualRetIncomeI.place(relx=0, rely=0.29, relwidth=1)
E_desAnnualRetIncomeI_ttp = CreateToolTip(E_desAnnualRetIncomeI, "Enter your desired annual retimrement income after active years i.e. after age 80 years")


L_averageAnnualReturnRate = tk.Entry(formEntryFrame, bg="white")
L_averageAnnualReturnRate.place(relx=0, rely=0.32, relwidth=1)
L_averageAnnualReturnRate_ttp = CreateToolTip(L_averageAnnualReturnRate, "Enter estimated average annual return rate")


B_calculateButton = tk.Button(form, text="Calculate")
B_calculateButton.place(relx=0.11, rely=0.43, relwidth=0.1)

B_resetButton = tk.Button(form, text="Reset")
B_resetButton.place(relx=0.26, rely=0.43, relwidth=0.1)





app.mainloop()