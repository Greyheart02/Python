from tkinter import *
import student_db_backend
from tkinter import ttk
import random
import tkinter.messagebox
import daytime
import pymysql
import time
import tempfile, os

class Student:
    def _init_(self, root):
        self.root = root
        blank_space=""
        esle.root.title(200 * blank_space + "Student Database Management System")

        StdID = StringVar()
        Firstname = StringVar()
        Surname= StringVar()
        DoB = StringVar()
        Age= StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile= StringVar()

        MainFrame = Frame(self.root, bd=10, idth= 1350, height= 700, relief= RIDGE, bg= "cadet blue")
        MainFrame.grid()

        TopFrame1= Frame(MainFrame, bd=5, width= 1340, height=50, relief=Ridge)
        TopFrame1.grid(row=2, column=0, pady=8)
        TitleFrame = Frame(MainFrame, bd=7, width= 1340, height=100, relief= RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3= Frame(MainFrame, bd, width= 1340, height= 500, relief= RIDGE)
        TopFrame3.grid(row=1, column=0)

        leftFrame = Frame(TopFrame3, bd=5, width= 1340, height=400, padx=2, bg= "cadet blue", relief= RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1= Frame(LeftFrame, bd=5, width=600, height=100, padx= 2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=Top, padx=0, pady=4)
        
        RightFrame1= Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg= "cadet blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a= Frame(RightFrame1, bd=5, width= 310, height=200, padx=2, pady=2, relief= RIDGE)
        RightFrame1a.pack(side=TOP)

        
        
        
