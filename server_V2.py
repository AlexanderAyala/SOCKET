#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket # for sockets
import sys
import os
from thread import * #agregamos paquete para la programacion por hilos

HOST = '' #Escuchara por todas las interfaces 
PORT = 4433 # Usamos un puerto de numeracion alta para no interferir

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket Creado"

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print "Error al crear Socket. Error code: " + str (msg[0]) + "Mensaje de Error: " + msg[1]
	sys.exit()
	
print "Enlace via Socket Activo"

s.listen(10) #Encolara un maximo de 10 conexiones
print "Socket escuchando en puerto " + str(PORT)

def hilo_cliente(conn):
	#enviar un mensaje al cliente cuando se conecte
	conn.send("Bienvenido al servidor. Escriba algo y presione ENTER ")
	conn.send("\n")
	conn.send("\n")
	conn.send("**Para ver una lista de palabras reservadas, ingrese: Lista")
	conn.send("\n")
	while True:
		#conn, addr = s.accept()
		#Muestra informacion del cliente
		#print "Conectado con " + addr[0] + ';' + str(addr[1])
	
		data = conn.recv(1024)
		    
		if data == "Lista":
			respuest =("Ingrese cualquiera de las siguientes palabras...\n\n-Aguacate      -Cratos         -Kernel          -Red\n-Archivos      -Debian         -Linux           -Sistema Operativo\n-CPU           -Directorio     -Plataforma      -Smartphone\n-Charamusca    -Fecha          -Python          -Version\n-Chilate       -Github         -RAM\n")
			respuesta = str(respuest)
			
		elif data == "hola" or data == "Hola" or data == "HOLA":
		    respuesta = "Hola, buen dia"
		
		elif data == "Como estas":
		    respuesta = "Bien..El mantenimiento no es tan malo..... no me quejo...\n"
		elif data == "Como te llamas":
		    respuesta = "Mi nombre es Cratos_Server"
		elif data == "Donde vives":
		    respuesta = "Soy como el gato de Schrodinger; estoy en todos lados y en ninguno a la vez"
		elif data == "Adios":
		    respuesta = "I'll be back"
		
		elif data =="Chilate":
		    respuesta="Bebida creada por los salvadoreños la cual contiene extracto de maiz, al cual se le mezcla agua y se convierte en una especie de atol; el cual se acompaña de un dulce de atado o batido de dulce. \n"
		
		elif data =="Python":
		    respuesta="Es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. \n"
		
		elif data =="Aguacate":
		    respuesta="Es una fruta rica en Vitamina E, antioxidantes, potasio, magnesio, fibra y carbohidratos complejos. \n"
		
		elif data =="Smartphone":
		    respuesta="Es un tipo de telefono movil construido sobre una plataforma informatica movil, con mayor capacidad de almacenar datos y realizar actividades, semejante a la de una minicomputadora. \n"
		
		elif data =="Sistema Operativo":
		    respuesta="Es un conjunto de órdenes y programas que controlan los procesos básicos de una computadora y permiten el funcionamiento de otros programas. \n"
		
		elif data =="Charamusca":
		    respuesta="Es refresco congelado en una bolsa plástica normalmente pequeña (aunque el tamaño puede variar). \n"
		    
		elif data == "Linux":
		    respuesta = "Es uno de los términos empleados para referirse a la combinación del núcleo o kernel libre similar a Unix denominado Linux con el sistema operativo GNU. \n"
		    
		elif data == "Github":
		    respuesta = "Es una plataforma de desarrollo colaborativo de software para alojar proyectos utilizando el sistema de control de versiones Git. El código se almacena de forma pública, aunque también se puede hacer de forma privada, creando una cuenta de pago. \n"
		
		elif data == "Debian":
		    respuesta = "Es una comunidad conformada por desarrolladores y usuarios, que mantiene un sistema operativo GNU basado en software libre. \n"
		
		elif data == "Cratos":
		    respuesta = "\nEn la mitologia griega, Cratos (en griego antiguo Κράτος Krátos, en latín Cratus) era la personificacion de la fuerza y del poder. Era hijo del titan Palas y de Estigia, y formaba parte del sequito de Zeus junto a su hermano Zelo y sus hermanas Bia y Nike. Participo en la lucha contra los gigantes (Gigantomaquia), y en la lucha contra los titanes (Titanomaquia). Fue quien ayudo a Hefesto y a Bia a encadenar y cegar a Prometeo cuando este fue sorprendido robando el fuego de los dioses para los hombres. \n"
		    
		
		elif data == "CPU" or data == "cpu":
			respuest = os.system("cat /proc/cpuinfo")
			respuesta = (str(respuest))
		
		elif data == "Fecha":
			respuest = os.system("date")
			respuesta = str(respuest)
		
		elif data == "Kernel":
			respuest = os.system("cat /proc/version")
			respuesta = str(respuest)
			
		elif data == "Red":
			respuest = os.system("cat /proc/net/dev")
			respuesta = str(respuest)
			
		elif data == "RAM" or data == "ram":
			respuest = os.system("cat /proc/net/meminfo")
			respuesta = str(respuest)
		
		elif data == "Archivos":
			respuest = os.system("ls -l")
			respuesta = str(respuest)
		
		elif data == "Directorio":
			respuest = os.getcwd()
			respuesta = str(respuest)
			
		elif data == "Version":
			respuest = sys.version
			respuesta = str(respuest)
		
		elif data == "Plataforma":
			respuest = sys.platform
			respuesta = str(respuest)
			
		    
		else:
			respuesta = "No puedo procesar su termino, intente con otra funcion o termine la conversacion"
		    
		#respuesta = "Yeah....." + data
		print data		
		if not data:
			break
		elif data == 'q':
			print "Recibi " + data + " tome una accion...."
		conn.sendall(respuesta)
	#cerrar conexion
	conn.close()

while 1:
	#espera para aceptar conexiones
	conn, addr = s.accept()
	print "conectado con " + addr[0] + ';' + str (addr[1])
	
	#inicia un nuevo hilo el cual recibe 2 parametros el hilo
	
	start_new_thread(hilo_cliente, (conn,))
s.close()
