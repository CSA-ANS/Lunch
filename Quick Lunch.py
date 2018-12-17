'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Read It
Version 1 .0
This is my quick lunch program
The user can choose a drink, entree, day of the week, and payment option. They will then calculate how much it costs and
enter their ID. It will save their checkout to a text file
'''

# Ammaar Siddiqui
# Advanced Computer Programming
# 12/17/18

from tkinter import *
from tkinter import ttk

class App:
    global x
    global y
    global z
    global a
    global b
    x=0
    y=0
    z=0
    a=0
    b=0
    def __init__(self, master, *args):
        self.menubar=Menu(master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=root.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.helpmenu=Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About")
        self.helpmenu.add_command(label="Instructions")
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        root.config(menu=self.menubar)
        content=Frame(root)
        self.drink_label = Label(content, text="Drink")
        radio_frame=Frame(content)
        drink.set(0)
        self.radio_1=Radiobutton(radio_frame, text="Soda", variable=drink, value="Soda", command=self.radio_progress)
        self.radio_2=Radiobutton(radio_frame, text="Tea", variable=drink, value="Tea", command=self.radio_progress)
        self.radio_3=Radiobutton(radio_frame, text="Milk", variable=drink, value="Milk", command=self.radio_progress)
        self.radio_4=Radiobutton(radio_frame, text="Juice", variable=drink, value="Juice", command=self.radio_progress)
        self.radio_5=Radiobutton(radio_frame, text="Bottled Water", variable=drink, value="Bottled Water", command=self.radio_progress)
        self.radio_1.pack()
        self.radio_2.pack()
        self.radio_3.pack()
        self.radio_4.pack()
        self.radio_5.pack()
        self.day_spin=Spinbox(content, state="readonly", wrap=True, textvariable=day, values=("Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
        self.payment = ttk.Combobox(content, values=["Credit", "Check", "Cash"], textvariable=pay_type, state='readonly')
        self.payment.bind('<<ComboboxSelected>>', self.combobox_progress)
        self.payment.bind('<FocusIn>', self.defocus)
        self.calc_b=Button(content, text="CALCULATE", command=self.calc)
        self.check_b=Button(content, text="CHECKOUT", command=self.checkout, state=DISABLED)
        self.entree_label=Label(content, text="Entrees")
        self.entree_lbox = Listbox(content, height=6, exportselection=FALSE)
        for c in ["Sandwich", "Pizza", "Chicken Nuggets", "Chicken", "Tofu", "Clam Chowder"]:
            self.entree_lbox.insert(END, c)
        self.entree_lbox.bind("<<ListboxSelect>>", self.lbox_progress)
        self.employee_label=Label(content, text="Employee ID")
        self.emp_ID=Entry(content)
        self.price_label=Label(content, text="Price: ")
        self.progress = ttk.Progressbar(content, orient=VERTICAL, length=200, mode='determinate')
        self.progress['value'] = x
        self.warning=Label(content)
        content.grid(column=0, row=0)
        self.drink_label.grid(column=0, row=0)
        radio_frame.grid(column=0, row=1, rowspan=3)
        self.day_spin.grid(column=0, row=4, pady=(0,20))
        self.payment.grid(column=0, row=5, pady=(0, 20))
        self.calc_b.grid(column=0, row=6, pady=(0, 20))
        self.check_b.grid(column=0, row=7)
        self.entree_label.grid(column=1, row=0, padx=(20, 0))
        self.entree_lbox.grid(column=1, row=1, columnspan=2, rowspan=3)
        self.employee_label.grid(column=1, row=5, padx=(20, 0))
        self.emp_ID.grid(column=2, row=5)
        self.price_label.grid(column=1, row=6, columnspan=2)
        self.warning.grid(column=1, row=7, columnspan=2)
        self.progress.grid(column=3, row=0, rowspan=7, padx=(20, 0))


        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)



    def calc(self):
        ID=self.emp_ID.get()
        space=True
        for x in ID:
            if x!=" ":
                space=False
        values = [self.entree_lbox.get(idx) for idx in self.entree_lbox.curselection()]
        if drink.get()==0:
            self.warning.config(text="Please choose a drink")
        elif values==[]:
            self.warning.config(text="Please choose an entree")
        elif self.emp_ID.get()=="" or space:
            self.warning.config(text="Please enter your ID")
        else:
            price=0
            if drink.get()=="Soda":
                price+=1
            elif drink.get()=="Tea":
                price+=1
            elif drink.get()=="Milk":
                price+=.75
            elif drink.get()=="Juice":
                price+=1.25
            elif drink.get()=="Bottled Water":
                price+=1
            if values[0]=="Sandwich":
                price+=3
            elif values[0]=="Pizza":
                price+=4
            elif values[0]=="Chicken Nuggets":
                price+=3.75
            elif values[0]=="Chicken":
                price+=4
            elif values[0]=="Tofu":
                price+=15
            elif values[0]=="Clam Chowder":
                price+=20
            total=price*1.0825
            rounded=round(total, 2)
            self.price_label.config(text="Price: $"+str(rounded))
            self.check_b.config(state="normal")
            self.calc_progress()
            self.warning.config(text="")


    def checkout(self):
        global x
        global y
        global z
        global a
        global b
        ID=self.emp_ID.get()
        space=True
        for x in ID:
            if x!=" ":
                space=False
        values = [self.entree_lbox.get(idx) for idx in self.entree_lbox.curselection()]
        if pay_type.get()=="":
            self.warning.config(text="Please choose a payment type")
        elif self.emp_ID.get()=="" or space:
            self.warning.config(text="Please enter your ID")
            self.check_b.config(state=DISABLED)
        else:
            price=0
            if drink.get()=="Soda":
                price+=1
            elif drink.get()=="Tea":
                price+=1
            elif drink.get()=="Milk":
                price+=.75
            elif drink.get()=="Juice":
                price+=1.25
            elif drink.get()=="Bottled Water":
                price+=1
            if values[0]=="Sandwich":
                price+=3
            elif values[0]=="Pizza":
                price+=4
            elif values[0]=="Chicken Nuggets":
                price+=3.75
            elif values[0]=="Chicken":
                price+=4
            elif values[0]=="Tofu":
                price+=15
            elif values[0]=="Clam Chowder":
                price+=20
            total=price*1.0825
            rounded=round(total, 2)
            file=open("lunches.txt", "a")
            message=(self.emp_ID.get()+"|||"+str(rounded))
            file.write(message+"\n")
            file.close()
            drink.set(0)
            day.set("Monday")
            pay_type.set("")
            self.entree_lbox.bind(self.entree_lbox.selection_clear(0, END))
            self.emp_ID.delete(0, END)
            self.price_label.config(text="Price:")
            self.progress.config(value=0)
            self.warning.config(text="")
            y=0
            x=0
            z=0
            a=0
            b=0

    def combobox_progress(self, event):
        global x
        global z
        z+=1
        if z==1:
            x = int(x) + 25
            self.progress['value'] = int(x)

    def radio_progress(self):
        global x
        global y
        y+=1
        if y==1:
            x = int(x) + 25
            self.progress['value'] = int(x)

    def lbox_progress(self, event):
        global x
        global a
        a+=1
        if a==1:
            x = int(x) + 25
            self.progress['value'] = int(x)

    def calc_progress(self):
        global x
        global b
        b+=1
        if b==1:
            x = int(x) + 25
            self.progress['value'] = int(x)

    def defocus(self, event):
        event.widget.master.focus_set()












root = Tk()
drink=StringVar()
day=StringVar()
pay_type=StringVar()
app = App(root, drink, day, pay_type)
root.title("Quick Lunch")
root.geometry("400x400")
root.minsize(400, 400)
root.mainloop()
root.destroy()