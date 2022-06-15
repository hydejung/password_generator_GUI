from struct import pack
from tkinter import *
import time
from tkinter import ttk, messagebox
import random

from matplotlib.pyplot import text

root = Tk()
root.title('Password Generator')
root.geometry('500x700')

#variable for password generate
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I',
           'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','&','*']

#random password generated list
password_list = []


# Name of Program Label
name_label = Label(root,text='Password Generator Program',font=('Tahoma',26,'bold'))
name_label.pack()

# Logo of Program
logo = PhotoImage(file='password.png')
logo_image = Label(root,image=logo)
logo_image.pack()

# Label input the total of letter for password generate
ask_letter_label = Label(root,text='How Many letter do you want in your password',font=(None,16))
ask_letter_label.pack()

#get the total letter
get_letter = StringVar()
letter_entry = ttk.Entry(root,textvariable=get_letter,font=(None,20))
letter_entry.pack()

# Label input the total of number for password generate
ask_number_label = Label(root,text='How Many number do you want in your password',font=(None,16))
ask_number_label.pack()

#get the total number
get_number = StringVar()
number_entry = ttk.Entry(root,textvariable=get_number,font=(None,20))
number_entry.pack()

# Label input the total of symbol for password generate
ask_symbol_label = Label(root,text='How Many symbol do you want in your password',font=(None,16))
ask_symbol_label.pack()

#get the total number
get_symbol = StringVar()
symbol_entry = ttk.Entry(root,textvariable=get_symbol,font=(None,20))
symbol_entry.pack()



def random_password():
      # pick letter
      int_get_letter = int(get_letter.get())
      for pick in range(0,int_get_letter):
            password_list.append(random.choice(letters))
      # pick number
      int_get_number = int(get_number.get())
      for pick in range(0,int_get_number):
            password_list.append(random.choice(numbers))
      int_get_symbol = int(get_symbol.get())
      for pick in range(0,int_get_symbol):
            password_list.append(random.choice(symbols))
      
      random.shuffle(password_list)
      password = ""
      for pick in password_list:
            password += pick
            
      msg_password = Label(root,text="Your Password is",font=(None,24)).place(x=160,y=470)
      
            
      result_password = Label(root,text=password,fg='red',font=(None,40,'bold')).place(x=150,y=510)
      
                  
      
b1 = ttk.Button(root,text='Generate Password',command=random_password)
b1.pack()


root.mainloop()