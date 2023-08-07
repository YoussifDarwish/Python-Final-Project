
from customtkinter import * 

master = CTk()
master.title("My Calculator")

def button_click(num):
    number = e.get()
    e.delete(0, END)
    e.insert(0, str(number) + str(num))

def button_add():
    first_number = e.get()
    global math 
    math = "add"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global math 
    math = "sub"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
def button_div():
    first_number = e.get()
    global math
    math = "div"
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    global math
    math = "mult"
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def clear():
    e.delete(0, END)

def equal():
    second_number = e.get()
    if math == "add":
        result = f_num + float(second_number)
    if math == "sub":
        result = f_num - float(second_number)
    if math == "div":
        result = f_num/ float(second_number)
    if math == "mult":
        result = f_num* float(second_number)
    e.delete(0, END)
    e.insert(0, str(result))


 #place where numbers show
e = CTkEntry(master, width= 300, border_width= 5)
e.grid(row = 0, column = 0, columnspan = 4)

#all the buttons needed and their function
button_1 = CTkButton(master, text= "1", command= lambda: button_click(1))
button_2 = CTkButton(master, text= "2", command= lambda: button_click(2))
button_3 = CTkButton(master, text= "3", command= lambda: button_click(3))
button_4 = CTkButton(master, text= "4", command= lambda: button_click(4))
button_5 = CTkButton(master, text= "5", command= lambda: button_click(5))
button_6 = CTkButton(master, text= "6", command= lambda: button_click(6))
button_7 = CTkButton(master, text= "7", command= lambda: button_click(7))
button_8 = CTkButton(master, text= "8", command= lambda: button_click(8))
button_9 = CTkButton(master, text= "9", command= lambda: button_click(9))
button_0 = CTkButton(master, text= "0", command= lambda: button_click(0))
button_addd = CTkButton(master, text= "+",  command= button_add)
button_subb = CTkButton(master, text= "-",  command= button_sub)
button_divide = CTkButton(master, text = "/", command= button_div)
button_multiply = CTkButton(master, text = "*", command= button_mult )
button_clear = CTkButton(master, text= "clear", width = 300,  command= clear)
button_equal = CTkButton(master, text= "equal",width = 300,  command= equal)

#normal width of a button is 140


#where to place all the buttons
button_7.grid(row = 1, column = 0,padx = 10, pady = 10)
button_8.grid(row = 1, column = 1, padx = 10, pady = 10)
button_9.grid(row = 1, column = 2, padx = 10, pady = 10)


button_4.grid(row = 2, column = 0, padx = 10, pady = 10)
button_5.grid(row = 2, column = 1, padx = 10, pady = 10)
button_6.grid(row = 2, column = 2, padx = 10, pady = 10)


button_1.grid(row = 3, column =0, padx = 10, pady = 10 )
button_2.grid(row = 3, column = 1, padx = 10, pady = 10)
button_3.grid(row = 3, column = 2, padx = 10, pady = 10)

button_0.grid(row = 4, column = 0, padx = 10, pady = 10)
button_clear.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2)

button_addd.grid(row = 5, column = 0, padx = 10, pady = 10)
button_equal.grid(row = 5, column = 1, padx = 10, pady = 10, columnspan = 2)

button_subb.grid(row = 6, column = 0, padx = 10, pady = 10 )
button_divide.grid(row = 6, column = 1, padx = 10, pady = 10)
button_multiply.grid(row = 6, column = 2, padx = 10, pady = 10)


    
    
    
    

    


#runs the app
master.mainloop()