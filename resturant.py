from tkinter import *


root = Tk()

root.geometry('1325x690+0+0')

root.resizable(0,0)

root.title('Resturant Management System By Jude')
root.config(bg='firebrick4')

topFrame=Frame(root, bd=10,relief=RIDGE, bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame, text='Resturant Management System', font=('arial', 30, 'bold'),  fg= 'yellow', bg='red4')
labelTitle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame, bd=4,relief=RIDGE, bg="firebrick4", pady= 10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame, text='Food', font=('arial',19, 'bold'),bd=10,relief=RIDGE, fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame, text='drinks', font=('arial',19, 'bold'),bd=10,relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame, text='cakes', font=('arial',19, 'bold'),bd=10,relief=RIDGE, fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root, bd=15, relief=RIDGE, bg="red4")
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame, bd=1, relief=RIDGE, bg="red4")
calculatorFrame.pack()

receiptFrame=Frame(rightFrame, bd=4, relief=RIDGE, bg="red4")
receiptFrame.pack()

buttonFrame=Frame(rightFrame, bd=3, relief=RIDGE, bg="red4")
buttonFrame.pack()

#functions

def garri():
    if var1.get()==1:
        textgarri.config(state=NORMAL)
        textgarri.delete(0, END)

        

var1 =StringVar()
var2 =StringVar()
var3 =StringVar()
var4 =StringVar()
var5 =StringVar()
var6 =StringVar()
var7 =StringVar()
var8 =StringVar()
var9 =StringVar()

var11 =StringVar()
var12 =StringVar()
var13 =StringVar()
var14 =StringVar()
var15 =StringVar()
var16 =StringVar()
var17 =StringVar()
var18 =StringVar()
var19 =StringVar()

var21 =StringVar()
var22 =StringVar()
var23 =StringVar()
var24 =StringVar()
var25 =StringVar()
var26 =StringVar()
var27 =StringVar()
var28 =StringVar()
var29 =StringVar()

e_garri=StringVar()
e_friedrice=StringVar()
e_beans=StringVar()
e_nkwobi=StringVar()
e_amala=StringVar()
e_chicken=StringVar()
e_jollofrice=StringVar()
e_peppersoup =StringVar()
e_fruitsalad=StringVar()

e_coke =StringVar()
e_fanta =StringVar()
e_powerhorse =StringVar()
e_pepsi=StringVar()
e_henessey =StringVar()
e_berryblast =StringVar()
e_gulder =StringVar()
e_fearless =StringVar()
e_pulpyorange =StringVar()

e_oreo =StringVar()
e_apple =StringVar()
e_kitkat =StringVar()
e_vanilla =StringVar()
e_banana =StringVar()
e_brownie =StringVar()
e_pineapple =StringVar()
e_chocolate =StringVar()
e_blackforest =StringVar()

e_garri.set("0")
e_friedrice.set("0")
e_beans.set("0")
e_nkwobi.set("0")
e_amala.set("0")
e_chicken.set("0")
e_peppersoup.set("0")
e_jollofrice.set("0")
e_fruitsalad.set("0")

e_coke.set("0")
e_fanta.set("0")
e_powerhorse.set("0")
e_pepsi.set("0")
e_henessey.set("0")
e_berryblast.set("0")
e_gulder.set("0")
e_fearless.set("0")
e_pulpyorange.set("0")

e_oreo.set("0")
e_apple.set("0")
e_kitkat.set("0")
e_vanilla.set("0")
e_banana.set("0")
e_brownie.set("0")
e_pineapple.set("0")
e_chocolate.set("0")
e_blackforest.set("0")

costoffoodvar =StringVar()
costofdrinksvar =StringVar()
costofcakesvar =StringVar()
subtotalvar =StringVar()
servicetaxvar =StringVar()
totalcostvar =StringVar()




garri=Checkbutton(foodFrame, text='Garri', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var1
                  ,command=garri)
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


#now inputting the entry fields for food

textgarri=Entry(foodFrame, font=('arial',18,'bold'),bd=7, state =DISABLED, width=6,textvariable=e_garri)
textgarri.grid(row=0,column=1)

textfriedrice=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_friedrice)
textfriedrice.grid(row=1,column=1)

textbeans=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_beans)
textbeans.grid(row=2,column=1)

textNkwobi=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_nkwobi)
textNkwobi.grid(row=3,column=1)

textpeppersoup=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_peppersoup)
textpeppersoup.grid(row=4,column=1)

textjollofrice=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_jollofrice)
textjollofrice.grid(row=5,column=1)

textAmala=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_amala)
textAmala.grid(row=6,column=1)

textChicken=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_chicken)
textChicken.grid(row=7,column=1)

textFruitSalad=Entry(foodFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_fruitsalad)
textFruitSalad.grid(row=8,column=1)


"""

now drink frame

"""

coke=Checkbutton(drinksFrame, text='Coke', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var11)
coke.grid(row=0,column=0, sticky=W)

fanta=Checkbutton(drinksFrame, text='Fanta', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var12)
fanta.grid(row=1,column=0, sticky=W)

powerhorse=Checkbutton(drinksFrame, text='Power', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var13)
powerhorse.grid(row=2,column=0,sticky=W)

pepsi=Checkbutton(drinksFrame, text='pepsi', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var14)
pepsi.grid(row=3,column=0,sticky=W)

henessey=Checkbutton(drinksFrame, text='Henessey', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var15)
henessey.grid(row=4,column=0,sticky=W)

berryblast=Checkbutton(drinksFrame, text='Berry', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var16)
berryblast.grid(row=5,column=0,sticky=W)

gulder=Checkbutton(drinksFrame, text='Gulder', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var17)
gulder.grid(row=6,column=0,sticky=W)

fearless=Checkbutton(drinksFrame, text='Fearless', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var18)
fearless.grid(row=7,column=0,sticky=W)

pulpyorange=Checkbutton(drinksFrame, text='Pulpy', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var19)
pulpyorange.grid(row=8,column=0,sticky=W)


#now inputting the entry fields for drinks

textcoke=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_coke)
textcoke.grid(row=0,column=1)

textfanta=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_fanta)
textfanta.grid(row=1,column=1)

textpowerhorse=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_powerhorse)
textpowerhorse.grid(row=2,column=1)

textpepsi=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_pepsi)
textpepsi.grid(row=3,column=1)

texthenessey=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_henessey)
texthenessey.grid(row=4,column=1)

textberryblast=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_berryblast)
textberryblast.grid(row=5,column=1)

textgulder=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_gulder)
textgulder.grid(row=6,column=1)

textfearless=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_fearless)
textfearless.grid(row=7,column=1)

textpulpyorange=Entry(drinksFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_pulpyorange)
textpulpyorange.grid(row=8,column=1)


"""

for cakes

"""

oreo=Checkbutton(cakesFrame, text='Oreo', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var21)
oreo.grid(row=0,column=0, sticky=W)

apple=Checkbutton(cakesFrame, text='Apple', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var22)
apple.grid(row=1,column=0, sticky=W)

kitkat=Checkbutton(cakesFrame, text='Kitkat', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var23)
kitkat.grid(row=2,column=0,sticky=W)

vanilla=Checkbutton(cakesFrame, text='Vanilla', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var24)
vanilla.grid(row=3,column=0,sticky=W)

banana=Checkbutton(cakesFrame, text='Banana', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var25)
banana.grid(row=4,column=0,sticky=W)

brownie=Checkbutton(cakesFrame, text='Brownie', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var26)
brownie.grid(row=5,column=0,sticky=W)

pineapple=Checkbutton(cakesFrame, text='Pineapple', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var27)
pineapple.grid(row=6,column=0,sticky=W)

chocolate=Checkbutton(cakesFrame, text='Chocolate', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var28)
chocolate.grid(row=7,column=0,sticky=W)

blackforest=Checkbutton(cakesFrame, text='Black forest', font=('arial', 18,'bold'),onvalue=1,offvalue=0, variable=var29)
blackforest.grid(row=8,column=0,sticky=W)

#now inputting the entry fields for cakes

textoreo=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownie=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textChocolate=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_chocolate)
textChocolate.grid(row=7,column=1)

textblackforest=Entry(cakesFrame, font=('arial',18,'bold'),bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)


#cosr of food labels and entey fields

labelCostofFood=Label(costFrame, text="Cost of Food", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelCostofFood.grid(row=0, column=0)
textCostofFood= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= costoffoodvar)
textCostofFood.grid(row=0, column=1, padx= 41)

labelCostofDrinks=Label(costFrame, text="Cost of Drinks", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelCostofDrinks.grid(row=1, column=0)
textCostofDrinks= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx= 41)

labelCostofCakes=Label(costFrame, text="Cost of Cakes", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelCostofCakes.grid(row=2, column=0)
textCostofCakes= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= costofcakesvar)
textCostofCakes.grid(row=2, column=1, padx= 41)

labelSubtotal=Label(costFrame, text="Sub Total", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelSubtotal.grid(row=0, column=2)
textSubtotal= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= subtotalvar)
textSubtotal.grid(row=0, column=3, padx= 41)

labelServiceTax=Label(costFrame, text="Service Tax", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelServiceTax.grid(row=1, column=2)
textServiceTax= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= servicetaxvar) 
textServiceTax.grid(row=1, column=3, padx= 41)

labelTotalCost=Label(costFrame, text="Total Cost", font=("arial", 16, "bold"), bg="firebrick4", fg="white" )
labelTotalCost.grid(row=2, column=2)
textTotalCost= Entry(costFrame, font=("ariai", 16, "bold"), bd= 6, width= 14, state= "readonly", textvariable= totalcostvar)
textTotalCost.grid(row=2, column=3, padx= 41)

#buttons

buttonTotal=Button(buttonFrame, text="Total", font=("arial", 14, "bold"), fg="white", bg="red4", bd=3, padx=5)
buttonTotal.grid(row=0, column=0)

buttonReceipt=Button(buttonFrame, text="Receipt", font=("arial", 14, "bold"), fg="white", bg="red4", bd=3, padx=5)
buttonReceipt.grid(row=0, column=1)

buttonSave=Button(buttonFrame, text="Save", font=("arial", 14, "bold"), fg="white", bg="red4", bd=3, padx=5)
buttonSave.grid(row=0, column=2)

buttonSend=Button(buttonFrame, text="Send", font=("arial", 14, "bold"), fg="white", bg="red4", bd=3, padx=5)
buttonSend.grid(row=0, column=3)

buttonReset=Button(buttonFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="red4", bd=3, padx=5)
buttonReset.grid(row=0, column=4)

#text area for receipt

textReceipt=Text(receiptFrame,font=("arial", 12, "bold"), bd=3, width=42, height= 14)
textReceipt.grid(row=0, column=0)

#calculator

operator="" #holds the values
def buttonClick(numbers):
    global operator
    operator= operator+ numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator=""
    calculatorField.delete(0,END)

def answer():
    global operator
    result= str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0,result)
    operator= ""
    


calculatorField=Entry(calculatorFrame, font=("arial", 16, "bold"), width= 33, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7= Button(calculatorFrame, text="7", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("7"))
button7.grid(row=1,column=0)

button8= Button(calculatorFrame, text="8", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("8"))
button8.grid(row=1,column=1)

button9= Button(calculatorFrame, text="9", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("9"))
button9.grid(row=1,column=2)

buttonPlus= Button(calculatorFrame, text="+", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                   command=lambda:buttonClick("+"))
buttonPlus.grid(row=1,column=3)

button4= Button(calculatorFrame, text="4", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("4"))
button4.grid(row=2,column=0)

button5= Button(calculatorFrame, text="5", font=("arial", 15, "bold"), fg="red", bg="white", bd=6, width=6,
                command=lambda:buttonClick("5"))
button5.grid(row=2,column=1)

button6= Button(calculatorFrame, text="6", font=("arial", 15, "bold"), fg="red", bg="white", bd=6, width=6,
                command=lambda:buttonClick("6"))
button6.grid(row=2,column=2)

buttonMinus= Button(calculatorFrame, text="-", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                    command=lambda:buttonClick("-"))
buttonMinus.grid(row=2,column=3)

button1= Button(calculatorFrame, text="1", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("1"))
button1.grid(row=3,column=0)

button2= Button(calculatorFrame, text="2", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("2"))
button2.grid(row=3,column=1)

button3= Button(calculatorFrame, text="3", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("3"))
button3.grid(row=3,column=2)

buttonMult= Button(calculatorFrame, text="*", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                   command=lambda:buttonClick("*"))
buttonMult.grid(row=3,column=3)

buttonAns= Button(calculatorFrame, text="Ans", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                  command=answer)
buttonAns.grid(row=4,column=0)

buttonClear= Button(calculatorFrame, text="Clear", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                    command=clear)
buttonClear.grid(row=4,column=1)

button0= Button(calculatorFrame, text="0", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                command=lambda:buttonClick("0"))
button0.grid(row=4,column=2)

buttonDiv= Button(calculatorFrame, text="/", font=("arial", 15, "bold"), fg="yellow", bg="red4", bd=6, width=6,
                  command=lambda:buttonClick("/"))
buttonDiv.grid(row=4,column=3)



"""
gitcoin.co/grants/cart/bulk-add/5940;0.0011;3,5688;0.0011;3,5288;0.0011;3,5051;0.0011;3,5007;0.0011;3,4665;0.0011;3,4268;0.0011;3,4201;0.0011;3,4019;0.0011;3,2575;0.0011;3,1773;0.0011;3,886;0.0011;3,821;0.0011;3,599;0.0011;3,331;0.0011;3,191;0.0011;3,12;0.0011;3,:timmie-israel
"""










