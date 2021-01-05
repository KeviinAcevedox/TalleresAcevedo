import socket
import threading
import sys
import json

class Cliente():

    molde_mensaje = {'id': 0, 'nombre': 'Cliente'}

    def __init__(self, host="localhost", puerto=3000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(puerto)))

        mensajes_recibidos = threading.Thread(target=self.mensajes_recibidos)

        mensajes_recibidos.daemon = True
        mensajes_recibidos.start()

        while True:
            mensaje = input()
            if mensaje != "salir":
                self.enviar_mensaje(mensaje)
            else:
                self.sock.close()
                sys.exit()



    def mensajes_recibidos(self):
        while True:
            try:
                datos = self.sock.recv(1024)
                if datos:
                    print("recibiendo")
                    print(datos.decode("utf-8"))
            except:
                pass

    def enviar_mensaje(self, mensaje):
        self.molde_mensaje['id'] = mensaje
        self.sock.send(bytes(json.dumps(self.molde_mensaje),encoding="utf-8"))


c = Cliente()