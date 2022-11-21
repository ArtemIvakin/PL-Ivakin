from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk, filedialog

def calc():
    a = int(0)
    n1 = ch1.get()
    n2 = ch2.get()
    zn = znak.get()
    if zn == '+':
       a= float(n1) + float(n2)
    elif zn == '-':
       a= float(n1) - float(n2)
    elif zn == '*':
       a= float(n1) * float(n2)
    elif zn == '/':
       a= float(n1) / float(n2)
    vivod['text']= a

def check():
    a = ck1.get()
    b = ck2.get()
    c = ck3.get()
    var1 = 'вы выбрали первый вариант'
    var2 = 'вы выбрали второй вариант'
    var3 = 'вы выбрали третий вариант'

    if a == 1 and b == 1 and c == 1:
        messagebox.showinfo('Внимение', 'Вы выбрали все три варианта.')
    elif a == 1 and b == 1:
        messagebox.showinfo('Внимение', 'вы выбрали первый и второй вариант')
    elif a == 1 and c == 1:
        messagebox.showinfo('Внимение', 'вы выбрали первый и третий вариант')
    elif b == 1 and c == 1:
        messagebox.showinfo('Внимение', 'вы выбрали второй и третий вариант')
    elif a == 1:
        messagebox.showinfo('Внимение', var1)
    elif b == 1:
        messagebox.showinfo('Внимение', var2)
    elif c == 1:
        messagebox.showinfo('Внимение', var3)
    else:
        messagebox.showinfo('Внимение', 'ошибка!: выберите хотя бы один.')

def text():
    F = filedialog.askopenfilename()
    with open(F, 'r+', encoding = 'utf-8-sig')as file:
        line = file.read()
        txt3.insert('1.0', line)
        txt3.place(x=0, y=0)



window = Tk()
window.title("Ivakin Artyom")
window.geometry('1000x600')
tab_control = ttk.Notebook(window)
calc1= ttk.Frame(tab_control)
tab_control.add(calc1, text = 'Калькулятор')
check1 = ttk.Frame(tab_control)
tab_control.add(check1, text = 'Чекбоксы')
text1 = ttk.Frame(tab_control)
tab_control.add(text1, text = 'Работа с текстом')
tab_control.pack(expand = 1, fill='both')



#калькулятор
ch1 = Entry(calc1,width=10)
ch2 = Entry(calc1,width=10)
znak = Combobox(calc1)
znak['values'] = ('+','-','*','/')
znak.current('0')
btn = Button(calc1, text="=", command=calc)
vivod = Label(calc1, text="")
ch1.grid(column=0, row=0)
znak.grid(column=1, row=0)
ch2.grid(column=2, row=0)
btn.grid(column=3, row=0)
vivod.grid(column=4, row=0)

# чекбоксы
ck1 = IntVar()
chk1 = Checkbutton(check1, text='1',  variable = ck1)
ck2 = IntVar()
chk2 = Checkbutton(check1, text='2',  variable = ck2)
ck3 = IntVar()
chk3 = Checkbutton(check1, text='3',  variable = ck3)
btnch = Button(check1, text="это хочу!", command=check)
chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)
btnch.grid(column=0, row=3)

#текст
menu = Menu(window)
item = Menu(menu)
menu.add_cascade(label='Файл', menu=item)
item.add_command(label='Загрузить файл', command = text)
window.config(menu=menu)
txt3 = Text(text1, width = 150, height = 150)

window.mainloop()