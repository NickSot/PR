import socket
import threading
import tkinter as tk

class ServerForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()
        self.clientsList = []

    def createWidgets(self):
        self.txtData = tk.Label(self, text = "")
        self.txtData.borderwidth = 100
        self.start = tk.Button(self)
        self.start["text"] = "Start"
        self.start["command"] = self.StartServer

        self.txtData.pack(side="top")
        self.start.pack(side = "bottom")

    def StartServer(self):
        server = socket.socket()

        self.clientsList = list()

        ip = "127.0.0.1"
        port = 5000

        server.bind((ip, port))

        server.listen(1)

        while True:
            client = server.accept()[0]
            
            self.clientsList.append(client)

            self.txtData.text = "Accepted " + client.getsockname()[0] + "!"

            t = threading.Thread(target = self.HandleClient, args = (self.clientsList, client, ))

            t.start()

    def HandleClient(self, clientsList, client):
        while True:
            data = client.recv(1024)

            if (data.decode("utf-8") == "q"):
                print(client.getsockname() + " left the room")

            self.BroadcastData(clientsList, data)

    def BroadcastData(self, clientsList, data):
        for client in clientsList:
            client.send(data)

def Main():
    form = ServerForm()
    
Main()
