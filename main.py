from tools import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def iniciar():
    print("Se ha presionado el botón 'Iniciar'")

def salir():
    root.destroy()

def obtener_seleccion():
    seleccionados = listbox.curselection()
    elementos_seleccionados = [columna_id[idx] for idx in seleccionados]
    publicaCion(elementos_seleccionados)

root = Tk() #VENTANA
root.title("PONETE LO KE KIERAS")
root.geometry("750x180")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = Frame(root) #FRAME
frame.grid(row=0, column=0, sticky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

botonIniciar = Button(frame, text="Iniciar", command=obtener_seleccion) #BOTONES
botonSalir = Button(frame, text="Salir", command=salir)
botonSalir.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
botonIniciar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

listbox=Listbox(frame,selectmode=MULTIPLE) #LISTBOX
listbox.grid(row=0,column=2)
columna_id = dataframe['ID']
columna_nombre = dataframe['NOMBRE']
for id, nombre in zip(columna_id, columna_nombre):
    item = f"{id} -{nombre}"
    listbox.insert(END, item)
max_width = max(len(item) for item in listbox.get(0,END))
listbox.configure(width=max_width)

scrollbar = Scrollbar(frame) #SCROLLBAR
scrollbar.grid(row=0,column=3,sticky=NS)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def actualizar_cantidad_seleccionados(): #LABEL ACTUALIZACION
    seleccionados = listbox.curselection()
    cantidad_seleccionados = len(seleccionados)
    label_cantidad.config(text=f"Seleccionados: {cantidad_seleccionados}")
label_cantidad = Label(frame)
label_cantidad.grid(row=1, column=2)
listbox.bind('<<ListboxSelect>>', lambda event: actualizar_cantidad_seleccionados())

frame.grid_rowconfigure(0, weight=1) # Configurar el diseño del contenedor principal
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)


root.mainloop()

