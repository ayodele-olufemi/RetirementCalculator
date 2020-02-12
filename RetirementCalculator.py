# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:43:13 2020

@author: ayyor
"""

import tkinter as tk

HEIGHT = 1080
WIDTH = 1920

app = tk.Tk()
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH, bg="#aecad0")
canvas.pack()


nav = tk.Frame(canvas, bg="#263D42")
nav.place(relwidth=1, relheight=0.1)


appName = tk.Label(nav, text="Retirement Calculator", font=("Helvetica 26 bold italic"), fg="white", bg="#263D42")  
appName.pack(expand=True)




app.mainloop()