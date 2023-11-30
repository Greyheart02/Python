from tkinter import *

root = Tk()

root.geometry('1200x690')

root.resizable(0,0)

root.title('Resturant Management System By Jude')
root.config(bg='firebrick4')


topFrame=Frame(root, bd=10,relief=RIDGE, bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame, text='Resturant Management System', font=('arial', 30, 'bold'),  fg= 'yellow', bg='red4')
labelTitle.grid(row=0,column=0)


menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(root,bd=4,relief=RIDGE)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame, text='Food', font=('arial',19, 'bold'),bd=10,relief=RIDGE, fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame, text='drinks', font=('arial',19, 'bold'),bd=10,relief=RIDGE)
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame, text='cakes', font=('arial',19, 'bold'),bd=10,relief=RIDGE)
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root, bd=15, relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame, bd=1, relief=RIDGE)
calculatorFrame.pack()

recieptFrame=Frame(rightFrame, bd=4, relief=RIDGE)
recieptFrame.pack()

buttonFrame=Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

var1 =StringVar()
var2 =StringVar()
var3 =StringVar()
var4 =StringVar()
var5 =StringVar()
var6 =StringVar()
var7 =StringVar()
var8 =StringVar()
var9 =StringVar()
var10 =StringVar()
var11 =StringVar()
var12 =StringVar()
var13=StringVar()
e_garri=StringVar()
e_friedrice=StringVar()
e_beans=StringVar()
e_Nkwobi=StringVar()
e_Amala=StringVar()
e_Chicken=StringVar()
e_FruitSalad=StringVar()
e_Beefjerky=StringVar()
e_Jollofrice=StringVar()
e_icecream=StringVar()
e_EweduSoup=StringVar()



garri=Checkbutton(foodFrame, text='Garri', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var1)
garri.grid(row=0,column=0, sticky=W)

friedrice=Checkbutton(foodFrame, text='Friedrice', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var2)
friedrice.grid(row=1,column=0, sticky=W)

beans=Checkbutton(foodFrame, text='Beans', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var3)
beans.grid(row=2,column=0,sticky=W)

Nkwobi=Checkbutton(foodFrame, text='Nkwobi', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var4)
Nkwobi.grid(row=3,column=0,sticky=W)

peppersoup=Checkbutton(foodFrame, text='peppersoup', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var5)
peppersoup.grid(row=4,column=0,sticky=W)

jollofrice=Checkbutton(foodFrame, text='Jollofrice', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var6)
jollofrice.grid(row=5,column=0,sticky=W)

Amala=Checkbutton(foodFrame, text='Amala', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var7)
Amala.grid(row=6,column=0,sticky=W)

Chicken=Checkbutton(foodFrame, text='Chicken', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var8)
Chicken.grid(row=7,column=0,sticky=W)

fruitsalad=Checkbutton(foodFrame, text='FruitSalad', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var9)
fruitsalad.grid(row=8,column=0,sticky=W)

Beefjerky=Checkbutton(foodFrame, text='Beefjerky', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var10)
Beefjerky.grid(row=9,column=0,sticky=W)

PoundedYam=Checkbutton(foodFrame, text='PoundedYam', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=1)
PoundedYam.grid(row=10,column=0,sticky=W)

icecream=Checkbutton(foodFrame, text='icecream', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var12)
icecream.grid(row=11,column=0,sticky=W)

Ewedu=Checkbutton(foodFrame, text='EweduSoup', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var13)
Ewedu.grid(row=12,column=0,sticky=W)

textgarri=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_garri)
textgarri.grid(row=0,column=1) 

friedrice=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_friedrice)
friedrice.grid(row=1,column=1) 

textbeans=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_beans)
textbeans.grid(row=2,column=1) 

textNkwobi=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_Nkwobi)
textNkwobi.grid(row=3,column=1)

textAmala=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_Amala)
textAmala.grid(row=4,column=1)

textChicken=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_Chicken)
textChicken.grid(row=5,column=1)

textFruitSalad=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_FruitSalad)
textFruitSalad.grid(row=6,column=1)

textBeefjerky=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_Beefjerky)
textBeefjerky.grid(row=7,column=1)

texticecream=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_icecream)
texticecream.grid(row=7,column=1)

textEwedu=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_EweduSoup)
textEwedu.grid(row=7,column=1)



