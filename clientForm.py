import socket
import threading
import tkinter as tk

class ClientForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.client = socket.socket()
        self.createWidgets()
        self.StartClient()

    def createWidgets(self):
        self.txtData = tk.Entry(self)
        self.txtMessage = tk.Entry(self)
        self.btnSend = tk.Button(self)
        self.btnSend["text"] = "Send"
        self.btnSend["command"] = lambda: self.SendData(self.client, self.txtData.get())
        
        self.txtData.pack(side="top")
        self.txtMessage.pack()
        self.btnSend.pack(side="bottom")

    def RecieveData(self, client):
        while True:
            data = client.recv(1024)

            self.txtMessage.textVariable = data.decode("utf-8")

            #print("\n" + data.decode("utf-8"))

    def SendData(self, client, data):
        client.send(data.encode("utf-8"))

    def StartClient(self):

        self.client.connect(("127.0.0.1", 5000))

        t = threading.Thread(target = self.RecieveData, args = (self.client, ))

        t.start()
        
        '''while True:
            t = threading.Thread(target = RecieveData, args = (client, ))
            t.start()
            msg = input("Insert message: ")

            if (msg == "q"):
                client.close()
                return
            
            client.send(msg.encode("utf-8"))

        client.close()'''

def Main():
    form = ClientForm()
    

Main()
