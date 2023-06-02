import pyautogui
import pyperclip
import subprocess
import time as ti


menu="https://www.facebook.com/marketplace/you/selling"
product="https://www.facebook.com/marketplace/create/item"

def combiKeys(tecla1,tecla2): #FUNCION PARA COMBINACION DE TECLAS
    pyautogui.keyDown(tecla1)
    ti.sleep(0.5)
    pyautogui.press(tecla2)
    pyautogui.keyUp(tecla1)

def abreEdge(): #ABRE NAVEGADOR
    subprocess.Popen("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    ti.sleep(1)
    combiKeys('win','up')

def abrePag(url): #SE LE PASA UNA URL COMO PARAMETRO PARA ABRIR EN EL NAVEGADOR
    pyautogui.click(2500,50)
    pyautogui.press('del')
    pyautogui.write(url)
    pyautogui.press('enter')
    ti.sleep(2)

def publica(titulo,precio,tipo,estado,talle,color,marca,descripcion,etiquetas): #PUBLICA ARTICULO

    listaTipos=[8,9,10,7,13]
    listaEstados=[1,2,0]
    
    pyautogui.moveTo(2329,300) #ESTA PAREJA MUEVE LA VENTANA DE TITULO A UN LUGAR ESPECIFICO
    pyautogui.scroll(-1200)
    
    pyautogui.moveTo(2100,250) #AQUI SE COLOCA EL TITULO
    ti.sleep(0.5)
    pyautogui.click()
    ti.sleep(1)
    pyautogui.write(str(titulo))
    ti.sleep(1)

    pyautogui.press('tab') #COLOCA PRECIO
    pyautogui.write(str(int(precio)))
    ti.sleep(1)

    pyautogui.press('tab') #DEFINE CATEGORIA
    ti.sleep(0.5)
    pyautogui.press('down')
    for i in range(listaTipos[int(tipo)-1]):
        pyautogui.press('tab')
        ti.sleep(0.25)
    ti.sleep(0.5)
    pyautogui.press('enter')

    pyautogui.press('tab') #DEFINE ESTADO
    ti.sleep(0.5)
    pyautogui.press('down')
    for i in range(listaEstados[int(estado)-1]):
        pyautogui.press('down')
        ti.sleep(0.25)
    pyautogui.press('enter')

    if tipo==1: #SI ES ROPA Y CALZADO DE MUJER
        pyautogui.press('tab',presses=2)
        ti.sleep(0.25)
        pyautogui.write(str(talle))  #COLOCA TALLE
        pyautogui.press('tab')
        ti.sleep(0.25)
        pyautogui.write(str(color))  #COLOCA COLOR
        pyautogui.press('tab')
        ti.sleep(0.25)
        pyautogui.write(str(marca))  #COLOCA MARCA
        pyautogui.press('tab',presses=2)
        ti.sleep(0.25)
    
    elif tipo==2: #SI ES ROPA Y CALZADO HOMBRE
        pyautogui.press('tab',presses=2)
        ti.sleep(0.25)
        pyautogui.write(str(talle))  #COLOCA TALLE
        pyautogui.press('tab',presses=3)
        ti.sleep(0.25)
        pyautogui.write(str(marca))  #COLOCA MARCA
        ti.sleep(0.25)
        pyautogui.press('tab')
        ti.sleep(0.25)
        
    elif tipo==3: #SI SON JOYAS Y ACCESORIOS
        pyautogui.press('tab',presses=6)
        ti.sleep(0.25)
    
    elif tipo==4: #SI SON BOLSOS
        pyautogui.press('tab',presses=2)
        ti.sleep(0.25)
        pyautogui.write(str(marca))  #COLOCA MARCA
        pyautogui.press('tab')
        ti.sleep(0.25)
        pyautogui.write(str(color))  #COLOCA COLOR
        ti.sleep(0.25)
        pyautogui.press('tab',presses=3)
        ti.sleep(0.25)
    
    elif tipo==5: #SI ES PARA BEBES Y NIÑOS
        pyautogui.press('tab',presses=2)
        ti.sleep(0.25)
        pyautogui.write(str(marca))  #COLOCA MARCA
        pyautogui.press('tab')
        ti.sleep(0.25) 


    pyperclip.copy(descripcion)#COLOCA DESCRIPCION
    combiKeys('ctrl','v')
    
    pyautogui.press('tab')
    ti.sleep(0.25)
    pyautogui.press('down')
    ti.sleep(0.25)
    pyautogui.press('up')
    ti.sleep(0.25)
    pyautogui.press('enter')#SELECCIONA ARTICULO UNICO
    ti.sleep(0.25)
    pyautogui.press('tab')
    pyautogui.write(str(etiquetas))  #COLOCA ETIQUETAS
    for i in range(5):
        pyautogui.press('tab')
        ti.sleep(0.25)
    pyautogui.press('space')
    ti.sleep(0.25)
    pyautogui.press('tab',presses=2)
    pyautogui.press('space')
    ti.sleep(3)
    pyautogui.click(2100,1045)
    ti.sleep(5)
    pyautogui.moveTo(2160,1045)
    combiKeys('shift','tab')
    ti.sleep(1)
    pyautogui.click()
    ti.sleep(0.25)
    pyautogui.press('tab')
    ti.sleep(0.25)
    pyautogui.press('tab')
    ti.sleep(0.25)
    #pyautogui.press('enter')  #al habilitar esta linea se publicara directamente
 


