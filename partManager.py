from tkinter import *
from tkinter import messagebox
from db import Database 
db = Database('store.ab')

app =Tk()#window object
app.title('Part Manager')
app.geometry('700x350')

def populateList():
    partList.delete(0, END)#delete before insertion is called, cause it will be used multiple times
    for row in db.fetch():#collect all data till the current row
        partList.insert(END, row)        

def addItem():
    if parttxt.get()=='' or customertxt.get()=='' or retailtxt.get()=='' or pricetxt.get()=='':
        messagebox.showerror('Required field','Please Fill Fields')
        return
    db.insert(parttxt.get(),customertxt.get(),retailtxt.get(),parttxt.get())#insert whats in the variable (Whatever entered in Entry)
    partList.delete(0, END)
    partList.insert(END,(parttxt.get(),customertxt.get(),retailtxt.get(),parttxt.get()))
    populateList()
#you stopped here bro
def removeItem():
    print("remove")

def updateItem():
    print("update")

def clearItem():
    print("clear")

parttxt = StringVar()
partLabel= Label(app, text='Part Name',font=('bold',12),pady=10,padx=10)#pady: space for grid from above
partLabel.grid(row=0,column=0,sticky=W)#sticky: stciker to left or right
partEntry=Entry(app, textvariable=parttxt)#textvariable you known that part
partEntry.grid(row=0,column=1)

customertxt = StringVar()
customerLabel= Label(app, text='Customer',font=('bold',12))#once pady is set it's automatically set for all 
customerLabel.grid(row=0,column=2,sticky=E)
customerEntry=Entry(app, textvariable=customertxt)
customerEntry.grid(row=0,column=3)

retailtxt = StringVar()
retailLabel= Label(app, text='Retailer',font=('bold',12),padx=10)
retailLabel.grid(row=1,column=0,sticky=W)
retailEntry=Entry(app, textvariable=retailtxt)
retailEntry.grid(row=1,column=1)

pricetxt = StringVar()
priceLabel= Label(app, text='Price',font=('bold',12))
priceLabel.grid(row=1,column=2,sticky=E)
priceEntry=Entry(app, textvariable=pricetxt)
priceEntry.grid(row=1,column=3)

partList= Listbox(app, height=10,width=80,border=0)#listboc creates a window/space in given geometry
partList.grid(row=3,column=0,columnspan=3,rowspan=3,pady=20,padx=20)
scrollBar=Scrollbar(app)
scrollBar.grid(row=3,column=3)
partList.configure(yscrollcommand=scrollBar.set)#setting parList and scrollbar together
scrollBar.configure(command=partList.yview)

addButton=Button(app,text='Add Part', width=10,command=addItem)
addButton.grid(row=2,column=0,pady=20)
removeButton=Button(app,text='Remove Part', width=10,command=removeItem)
removeButton.grid(row=2,column=1)
updateButton=Button(app,text='Update Part', width=10,command=updateItem)
updateButton.grid(row=2,column=2)
clearButton=Button(app,text='Clear Part', width=10,command=clearItem)
clearButton.grid(row=2,column=3)


app.mainloop()