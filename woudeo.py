from tkinter import *
import random

root=Tk()
root.title("hhihih")
root.geometry("500x600")

enter_name = Entry(root)
enter_name.place(relx= 0.5,rely = 0.1, anchor = CENTER)

enter_cap = Entry(root)
enter_cap.place(relx= 0.5,rely = 0.2, anchor = CENTER)

count_list = Label(root)
cap_list = Label(root)
rengcount = Label(root)
rengcap = Label(root)

list1 = []
list2 = []
def addcountcap() :
    count_name = enter_name.get()
    list1.append(count_name)
    cap_name = enter_cap.get()
    list2.append(cap_name)
    count_list["text"] = "Countries : " + str(list1)
    cap_list["text"] = "Capitals : " + str(list2)
    enter_name.delete(0, 'end')
    enter_cap.delete(0, 'end')
    
def rng():
    lenght = len(list1)
    randng = random.randint(0, lenght-1)
    gen_count = list1[randng]
    lenght1 = len(list2)
    randng1 = random.randint(0, lenght1-1)
    gen_cap = list2[randng1]
    rengcap["text"] = "Random Capital : " + gen_cap
    rengcount["text"] = "Random Country : " + gen_count
    
btn = Button(root, text="Add Country and Capital", command=addcountcap)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

count_list.place(relx=0.5,rely=0.4,anchor=CENTER)
cap_list.place(relx= 0.5,rely = 0.5, anchor = CENTER)

btn1 = Button(root, text="Show random Country and Capital", command=rng)
btn1.place(relx=0.5,rely=0.6,ancho=CENTER)

rengcount.place(relx= 0.5,rely = 0.7, anchor = CENTER)
rengcap.place(relx= 0.5,rely = 0.8, anchor = CENTER)

root.mainloop()
    
    