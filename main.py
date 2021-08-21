from tkinter import *
from tkinter import ttk

# color #
cor1 = "#123c80"
cor2 = "#edf0f2"
cor3 = "#4f0087"
cor4 = "#0af5d5"
cor5 = "#00e03c"


window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=cor1)

## frame ##
frame_screen = Frame(window, width=235, height=50, bg=cor5)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# all values  #

todos_valores = ''

#  function #


def receive_values(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valores_texto.set(todos_valores)

#  function #


def calcular_valor():
    global todos_valores
    resultado = eval(todos_valores)
    valores_texto.set(str(resultado))


#  function #
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valores_texto.set("")


# label#
valores_texto = StringVar()
# screen   #
app_screen = Label(frame_screen, textvariable=valores_texto, width=16, height=2, padx=7,
                   relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor5, fg=cor2)
app_screen.place(x=0, y=0)
## button ##

b_1 = Button(frame_body, command=limpar_tela, text="C", width=11, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, command=lambda: receive_values('%'), text="%", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_2.place(x=118, y=0)

b_3 = Button(frame_body, command=lambda: receive_values('/'), text="/", width=5, height=2, bg=cor4, fg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_3.place(x=177, y=0)

b_4 = Button(frame_body,  command=lambda: receive_values('7'), text="7", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_4.place(x=0, y=52)


b_5 = Button(frame_body, command=lambda: receive_values('8'), text="8", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_5.place(x=59, y=52)


b_5 = Button(frame_body, command=lambda: receive_values('9'), text="9", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_5.place(x=118, y=52)


b_6 = Button(frame_body, command=lambda: receive_values('*'), text="*", width=5, height=2, bg=cor4, fg=cor3,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_6.place(x=177, y=52)


b_7 = Button(frame_body, command=lambda: receive_values('4'), text="4", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_7.place(x=0, y=104)


b_8 = Button(frame_body, command=lambda: receive_values('5'), text="5", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_8.place(x=59, y=104)


b_9 = Button(frame_body, command=lambda: receive_values('6'),  text="6", width=5, height=2, bg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_9.place(x=118, y=104)


b_10 = Button(frame_body, command=lambda: receive_values('-'), text="-", width=5, height=2, bg=cor4, fg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_10.place(x=177, y=104)


b_11 = Button(frame_body, command=lambda: receive_values('1'), text="1", width=5, height=2, bg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_11.place(x=0, y=156)


b_12 = Button(frame_body, command=lambda: receive_values('2'),  text="2", width=5, height=2, bg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_12.place(x=59, y=156)


b_13 = Button(frame_body, command=lambda: receive_values('3'),  text="3", width=5, height=2, bg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_13.place(x=118, y=156)


b_14 = Button(frame_body, command=lambda: receive_values('+'), text="+", width=5, height=2, bg=cor4, fg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_14.place(x=177, y=156)


b_15 = Button(frame_body, command=lambda: receive_values('0'), text="0", width=11, height=2, bg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=0, y=208)

b_16 = Button(frame_body, command=lambda: receive_values('.'),  text=".", width=5, height=2, bg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_16.place(x=118, y=208)

b_17 = Button(frame_body, command=calcular_valor,  text="=", width=5, height=2, bg=cor4, fg=cor3,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)

b_17.place(x=177, y=208)

window.mainloop()
