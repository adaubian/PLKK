from loadFb import *
import pandas as pd
from tkinter import messagebox

nombre=""
precio=0
tipo=0
estado=0
talle=""
color=""
marca=""
descripcion=""
etiquetas=""

enlace_sheets = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSjOGfVt0inJVHpZ_uaoXhf6Ft2k1jfoY7TpiP3d7ltHG7gBW0lJHiVY4wAdv96IYmhip26KeIdvfhb/pub?gid=412029084&single=true&output=csv'
dataframe = pd.read_csv(enlace_sheets)

def obtieneDatos(ID):
    
    global id_buscar,nombre,precio,tipo,estado,talle,color,marca,descripcion,etiquetas

    id_buscar = ID
    registro = dataframe.loc[dataframe['ID'] == id_buscar]
    nombre = registro['NOMBRE'].values[0]
    precio = registro['PRECIO'].values[0]
    tipo = registro['TIPO'].values[0]
    estado = registro['ESTADO'].values[0]
    talle = registro['TALLE'].values[0]
    color = registro['COLOR'].values[0]
    marca = registro['MARCA'].values[0]
    descripcion = registro['DESCRIPCION'].values[0]
    etiquetas = registro['ETIQUETAS'].values[0]

    if str(talle)=="nan":
        talle=""
    if str(color)=="nan":
        color=""
    if str(marca)=="nan":
        marca=""
    
def publicaCion(prendas): #SECUENCIA COMPLETA DE PUBLICACION
    
    abreEdge()
    ti.sleep(2)
    abrePag(product)
    ti.sleep(0.25)
    for i in range(len(prendas)-1):
        pyautogui.keyDown('shift')
        combiKeys('ctrl','k')
        pyautogui.keyUp('shift')
        ti.sleep(1)
    combiKeys('ctrl','tab')
  
    for prenda in prendas:
        obtieneDatos(prenda)
        ti.sleep(2)
        pyautogui.click(2150,400)
        messagebox.showinfo("PLKK",f"Por favor selecciona las fotos de {id_buscar}") #CARGA FOTOS DEL ARTICULO
        pyautogui.click(3600,10)
        combiKeys('ctrl','tab')
  
    for prenda in prendas:
        publica(nombre,precio,tipo,estado,talle,color,marca,descripcion,etiquetas)






