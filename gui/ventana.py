import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

#ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Control Pan & Tilt")

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
btn_flechaArriba=tk.Button(ventanaPrincipal,image=fecha_Arriba)
btn_flechaArriba.grid(row=30, column=30)

btn_flechaArriba=tk.Button(ventanaPrincipal,image=fecha_Abajo)
btn_flechaArriba.grid(row=60, column=30)

btn_flechaDerecha=tk.Button(ventanaPrincipal,image=fecha_Derecha)
btn_flechaDerecha.grid(row=45, column=40)

btn_flechaIzquierda=tk.Button(ventanaPrincipal,image=fecha_Izquierda)
btn_flechaIzquierda.grid(row=45, column=10)


ventanaPrincipal.mainloop()