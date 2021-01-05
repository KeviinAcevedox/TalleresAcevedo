import socket
import threading
import sys
import pickle

class Servidor():
    def __init__(self, host="localhost", puerto=3000):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(puerto)))
        self.sock.listen(5)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptar_conexiones)
        procesar = threading.Thread(target=self.procesar_conexiones)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            mensaje = input()
            if mensaje != "salir":
                self.enviar_mensaje(mensaje)
            else:
                self.sock.close()
                sys.exit()


    def enviar_mensaje_todos(self, mensaje, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(pickle.dumps(mensaje))
            except:
                self.clientes.remove(c)

    def enviar_mensaje(self, mensaje):
        try:
            self.clientes[0].send(pickle.dumps(mensaje))
        except:
            pass


    def aceptar_conexiones(self):
        while True:
            try:
                conexion, direccion = self.sock.accept()
                conexion.setblocking(False)
                self.clientes.append(conexion)
                print("Cliente conectado")
            except:
                pass




    def procesar_conexiones(self):
        print ("EMPEZANDO A CONTROLAR LAS CONEXIONES..")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        datos = c.recv(1024)
                        if datos:
                            print(pickle.loads(datos))
                    except:
                        pass
s = Servidor()
