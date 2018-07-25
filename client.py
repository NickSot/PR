import socket
import threading

def RecieveData(client):
    while True:
        data = client.recv(1024)

        print("\n" + data.decode("utf-8"))

def Main():

    client = socket.socket()

    client.connect(("127.0.0.1", 5000))

    while True:
        t = threading.Thread(target = RecieveData, args = (client, ))
        t.start()
        msg = input("Insert message: ")

        if (msg == "q"):
            client.close()
            return
        
        client.send(msg.encode("utf-8"))

    client.close()

Main()
