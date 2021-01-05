import socket
import threading
import sys
import json

class Servidor():

    molde_mensaje = {'id': 0, 'nombre': 'Servidor'}

    def __init__(self, host="localhost", puerto=3000):
        self.cliente = None
        self.conexionEstablecida = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(puerto)))
        self.sock.listen(5)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptar_conexiones)
        procesar = threading.Thread(target=self.procesar_conexion)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            if(self.conexionEstablecida):
                mensaje = input()
                if mensaje != "salir":
                    self.enviar_mensaje(mensaje)
                else:
                    self.sock.close()
                    sys.exit()

    def aceptar_conexiones(self):
        print("ESPERANDO UNA CONEXIÓN...\n")
        while True:
            try:
                conexion, direccion = self.sock.accept()
                conexion.setblocking(False)
                self.cliente = conexion
                self.conexionEstablecida = True
                print("NUEVO CLIENTE CONECTADO...\n")
            except:
                pass


    def enviar_mensaje(self, mensaje):
        self.molde_mensaje['id'] = mensaje
        try:
            if self.conexionEstablecida:
                self.sock.send(bytes(json.dumps(self.molde_mensaje), encoding="utf-8"))
        except:
            pass


    def procesar_conexion(self):
        while True:
            try:
                datos = self.cliente.recv(1024)
                if datos:
                    print(datos.decode("utf-8"))
            except:
                pass
s = Servidor()
