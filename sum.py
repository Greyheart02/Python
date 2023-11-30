from tkinter import *

window=Tk()
window.title("My Average and variance")
window.geometry('500x300')

label1=Label(window, text='Enter First Number:', fg='blue', font=('Arial', 14))
label1.grid(row=0, column=0, padx=5, pady=10)

label1=Label(window, text='Enter Second Number:', fg='blue', font=('Arial', 14))
label1.grid(row=1, column=0, padx=5, pady=10)

label1=Label(window, text='Enter Third Number:', fg='blue', font=('Arial', 14))
label1.grid(row=2, column=0, padx=5, pady=10)

label1=Label(window, text='Enter Forth Number:', fg='blue', font=('Arial', 14))
label1.grid(row=3, column=0, padx=5, pady=10)




firstNum = IntVar()
secondNum = IntVar()
thirdNum = IntVar()
forthNum = IntVar()

textbox1=Entry(window, textvariable = firstNum, fg='blue', font=('Arial', 14))
textbox1.grid(row=0, column=1)

textbox2=Entry(window, textvariable = secondNum, fg='blue', font=('Arial', 14))
textbox2.grid(row=1, column=1)

textbox3=Entry(window, textvariable = thirdNum, fg='blue', font=('Arial', 14))
textbox3.grid(row=2, column=1)

textbox4=Entry(window, textvariable = forthNum, fg='blue', font=('Arial', 14))
textbox4.grid(row=3, column=1)




def myMean():
    myMean= (firstNum.get()+ secondNum.get() + thirdNum.get() + forthNum.get())/4
    label2.config(text='The Mean is:'+str(myMean))

def myVar():
        myMean= (firstNum.get()+ secondNum.get() + thirdNum.get() + forthNum.get())/4
        myVar = (firstNum.get()- myMean)**2 + (secondNum.get()- myMean)**2 + (thirdNum.get()-myMean)**2 + (forthNum.get()-myMean)**2
        label2.config(text='The Variance is:'+str(myVar))


button1=Button(window, command=myMean, text='Calculate average', fg='blue', font=('Arial', 14))
button1.grid(row=4, column=1, sticky=W)

button2=Button(window, command=myVar, text='Calculate mean', fg='blue', font=('Arial', 14))
button2.grid(row=5, column=1, sticky=W)

label2=Label(window, fg='green', font=('Arial', 14))
label2.grid(row=4, column=1, sticky=W)

                                                           
window.mainloop()
