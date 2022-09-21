#Librerias
from tkinter import *
import time

#Ventana
ventana = Tk()
ventana.title("Pomodoro timer")
ventana.geometry("600x400")
ventana.config(bg="black")
#No se puede ampliar ni encoger el programa en culaquier eje(x,y)
ventana.resizable(False,False)

#Titulo del programa
Titulo=Label(ventana,text="Pomodoro Timer",font="arial 20 bold",bg="red",fg="white")
Titulo.pack(padx=10)

#Reloj dentro del programa
Label(ventana,font=("arial",12,"bold"),text="Tiempo concurrido:",bg="White").place(x=170,y=70)

def reloj():
    reloj_tiempo = time.strftime("%H:%M:%S %p")
    hora_actual.config(text=reloj_tiempo)
    hora_actual.after(1000,reloj)

hora_actual=Label(ventana,font=("arial",12,"bold"),text="",fg="black",bg="white")
hora_actual.place(x=321,y=70)
reloj()


#Pomodoro
hora = StringVar()
Entry(ventana,textvariable=hora,width=2,font="arial 50",bg="black",fg="#fff",bd=0).place(x=130,y=120)
hora.set("00")

minu = StringVar()
Entry(ventana,textvariable=minu,width=2,font="arial 50",bg="black",fg="#fff",bd=0).place(x=250,y=120)
minu.set("00")

seg = StringVar()
Entry(ventana,textvariable=seg,width=2,font="arial 50",bg="black",fg="#fff",bd=0).place(x=370,y=120)
seg.set("00")

Label(ventana,text="horas",font="arial 12",bg="black",fg="#fff").place(x=205,y=180)
Label(ventana,text="minutos",font="arial 12",bg="black",fg="#fff").place(x=320,y=180)
Label(ventana,text="segundos",font="arial 12",bg="black",fg="#fff").place(x=445,y=180)

#Funciones
def Pomodoro():
    tiempo = int(hora.get())*3600 +int(minu.get())*60+int(seg.get())
    while tiempo > -1:
        minuto ,segundo = (tiempo//60, tiempo%60)
        
        horas = 0

        if minuto>60:
            horas,minuto=(minuto//60,minuto%60)

        seg.set(segundo)
        minu.set(minuto)
        hora.set(horas)

        ventana.update()
        time.sleep(1)

        if (tiempo == 0):
            seg.set("00")
            minu.set("00")
            hora.set("00")

        tiempo -= 1




#Botones
boton1 = Button(ventana,text="Iniciar",bg="green",bd=0,fg="#fff",width=10,height=2,font="arial 10 bold",command=Pomodoro)
boton1.pack(padx=4,pady=20,side=BOTTOM)

boton2 = Button(ventana,text="Salir",bg="red",fg="white",width=5,font="arial 10 bold",command=ventana.destroy)
boton2.place(x=520,y=350)

ventana.mainloop()
"""Si hablas español , puedes editar este codigo :p"""
