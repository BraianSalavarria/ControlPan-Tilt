import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

#funciones de tecla
def tecla_presionada(event):
    if event.keysym == "Up":
        btn_flechaArriba.config(relief=tk.SUNKEN)
        ventanaPrincipal.after(100, lambda: btn_flechaArriba.config(relief=tk.RAISED))
        funcionEjemplo("arriba")

    elif event.keysym =="Down":
        btn_flechaAbajo.config(relief=tk.SUNKEN)
        ventanaPrincipal.after(100, lambda: btn_flechaAbajo.config(relief=tk.RAISED))
        funcionEjemplo("abajo")

    elif event.keysym == "Left":
        btn_flechaIzquierda.config(relief=tk.SUNKEN)
        ventanaPrincipal.after(100, lambda: btn_flechaIzquierda.config(relief=tk.RAISED))
        funcionEjemplo("izquierda")

    elif event.keysym == "Right":
        btn_flechaDerecha.config(relief=tk.SUNKEN)
        ventanaPrincipal.after(100, lambda: btn_flechaDerecha.config(relief=tk.RAISED))
        funcionEjemplo("derecha")    

def funcionEjemplo(valor):
    print(valor)
    
#ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Control Pan & Tilt")
ventanaPrincipal.bind("<Key>", tecla_presionada)

#hacemos compatibles las imagenes
imagen1 = Image.open("iconos/flecha-arriba.png")
fecha_Arriba = ImageTk.PhotoImage(imagen1)

imagen2 = Image.open("iconos/flecha-hacia-abajo.png")
fecha_Abajo = ImageTk.PhotoImage(imagen2)

imagen3 = Image.open("iconos/flecha-derecha.png")
fecha_Derecha = ImageTk.PhotoImage(imagen3)

imagen4 = Image.open("iconos/flecha-izquierda.png")
fecha_Izquierda = ImageTk.PhotoImage(imagen4)


#creamos los botones y les asignamos las imagenes
btn_flechaArriba=tk.Button(ventanaPrincipal,image=fecha_Arriba, command=lambda: funcionEjemplo("arriba"))
btn_flechaArriba.grid(row=30, column=30)

btn_flechaAbajo=tk.Button(ventanaPrincipal,image=fecha_Abajo, command=lambda: funcionEjemplo("abajo"))
btn_flechaAbajo.grid(row=60, column=30)

btn_flechaDerecha=tk.Button(ventanaPrincipal,image=fecha_Derecha,command=lambda: funcionEjemplo("derecha"))
btn_flechaDerecha.grid(row=45, column=40)

btn_flechaIzquierda=tk.Button(ventanaPrincipal,image=fecha_Izquierda,  command=lambda: funcionEjemplo("izquierda"))
btn_flechaIzquierda.grid(row=45, column=10)


ventanaPrincipal.mainloop()