
#Importing Required Modules

from tkinter import *

#Creating a Function for Conversion

def main():

    # Creating a function help

    def help_(event):
        w1=Tk()
        w1.geometry('300x600+500+100')
        w1.title('help'.title())
        w1.configure(bg='light yellow')
        w1.iconbitmap(r"C:\Users\kakar\Desktop\Icons\help icon.ico")
        text=''' A  :  .-\n B  :  -...\n C  :  -.-.\n D  :  -..\n E  :  .\n F  :  ..-.\n G  :  --.\n H  :  ....
 I  :  ..\n J   :  .---\n K  :  -.-\n L   :  .-..\n M :  --\n N  :  -.\n O  :  ---\n P  :  .-..\n Q  :  --.-\n R  :  .-.
 S  :  ...\n T  :  -\n U  :  ..-\n V  :  ...-\n W :  .--\n X  :  -..-\n Y  :  -.--\n Z  :  --..'''
        txt1=Text(w1,height=28,width=20)
        txt1.insert(INSERT,'Morse Code Index\n')
        txt1.insert(INSERT,text)
        txt1.config(fg='red',font=('times new roman',13,'bold'),state='disabled')
        txt1.pack(pady=25)
        w1.mainloop()

    #Destroying entry_window

    global entry_window
    entry_window.destroy()

    #Function when Morse to English Radio Button is pressed

    def morse_to_eng():
        global lb4
        lb2=Label(window,text='MORSE TEXT : ',bg='blue',fg='white',font=('Calibri',12,'bold')).place(x=10,y=50)
        lb3=Label(window,text='ENGLISH TEXT: ',bg='blue',fg='white',font=('Calibri',12,'bold')).place(x=10,y=150)
        lb4=Label(window,text="NOTE: 1.Give one space for each letter in Morse Code\n2. Give ' , ' at the starting of next word   \nEx: .... .. ,.... --- .--      "
                  ,bg='yellow',fg='red')
        lb4.place(x=200,y=250)
        en1.focus()

    #Function when English to Morse Radio Button is pressed

    def eng_to_morse():
        lb2=Label(window,text='ENGLISH TEXT : ',bg='blue',fg='white',font=('Calibri',12,'bold')).place(x=10,y=50)
        lb3=Label(window,text='MORSE TEXT : ',bg='blue',fg='white',font=('Calibri',12,'bold')).place(x=10,y=150)
        lb4.config(text="",bg='skyblue')
        en1.focus()

    #Creating a Window

    window=Tk()
    window.geometry('800x300+500+300')
    window.title('MORSE CODE APP')
    window.iconbitmap(r'C:\Users\kakar\Desktop\Icons\preview.ico')
    window.configure(bg='skyblue')

    window.after(1, lambda: window.focus_force())

    #Creating Heading Label

    lb1=Label(window,text='MORSE CODE CONVERTER',font =("verdana", 12,'italic'))
    lb1.place(x=250,y=10)

    # Creating a label for help

    lb5=Label(window,text='Press F2 for Help'.title()).place(x=600,y=260)

    #Creating an Entry Box for Input

    en1=Entry(window,width=50)
    en1.place(x=170,y=50)
    
    #Creating a Variable (IntVar) to check which radio button is checked

    var=IntVar()

    #Creating a function to Translate the Input

    def translate(event):
        global text

        eng=en1.get().upper()  #Getting the input in upper case

        a=""   # creating a variable for the output

        # Defining a Dictionary for Morse Code

        morse_dict={'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}

        choice=var.get()

        #Creating a function to get English letter for a letter in Morse code

        def get_key(val):
            for key, value in morse_dict.items():
                 if val == value:
                     return key

        # Checking Morse to English radio button is checked and if true what to do
        
        if choice==1:
                for letter in eng.split(' '):
                    if ',' in letter:
                        a+=' '
                        a+=str(get_key(letter[1:len(letter)]))
                    
                    else:
                        a+=str(get_key(letter))

        # Checking English to Morse radio button is checked and if true what to do

        if choice==2:
            for letter in eng:
                if letter in list(morse_dict.keys()):
                    a+=morse_dict.get(letter)
                    a+=' '
                elif letter.isspace()==True:
                    a+=' '*3

        # Creating a Text Widget to display the output

        text=Text(window,height=5)
        text.insert(INSERT,a)
        text.place(x=130,y=150)

    # Defining a function erase input and output fields

    def delete():
        en1.delete(0,'end')
        text.delete("1.0",'end')

    # Creating a Button to translate input

    btn1=Button(window,text='Translate',bg='light cyan',fg='green',font=('arial',11,'bold'),command=window.bind('<Return>',translate))
    btn1.place(x=170,y=100)
    btn1.bind('<Button-1>',translate)

    # Creating a Button to exit application

    btn2=Button(window,text='Quit',bg='red',fg='white',font=('arial',11,'bold'),command=window.destroy).place(x=350,y=100)

    # Creating a Button to erase input and output fields

    btn3=Button(window,text='Clear',font=('arial',11,'bold'),command=delete).place(x=280,y=100)

    # Creating a Button to choose Morse to English Converter

    btn4=Radiobutton(window,text='Morse Code to English',variable=var,value=1,command=morse_to_eng)
    btn4.place(x=420,y=100)
    btn4.invoke()

    # Creating a Button to choose English to Morse Converter

    btn5=Radiobutton(window,text='English to Morse Code',variable=var,value=2,command=eng_to_morse)
    btn5.place(x=580,y=100)

    #Binding the window to get help window

    window.bind('<F2>',help_)

    window.mainloop()

#Creating an Entry Window to enter into Morse Code Environment

entry_window=Tk()
entry_window.geometry('700x300+500+300')
entry_window.title('MORSE CODE APP')
entry_window.iconbitmap(r'C:\Users\kakar\Desktop\Icons\preview.ico')
entry_window.config(bg='light green')

text11='welcome to morse code converter app'
text12='to enter into morse code converter environment \nplease click the button below'

# Creating a Welcome Heading

lb11=Label(entry_window,text=text11.title(),bg='blue',fg='white',font=('times new roman',18))
lb11.pack(pady=60,ipady=10,ipadx=50)

# Navigating the User to App

lb12=Label(entry_window,text=text12.title(),bg='orange',fg='red',font=11)
lb12.place(x=120,y=130)

# Creating a Button to Enter into Main Application

btn11=Button(entry_window,text='enter into app'.title(),bg='pink',fg='blue',command=lambda:main())
btn11.place(x=300,y=200)

# Creating a Label showing designed by kakarla sarathchandra reddy

lb13=Label(entry_window,text='designed by Kakarla sarathchandra reddy'.upper(),bg='purple',fg='white')
lb13.place(x=400,y=260)

entry_window.mainloop()
