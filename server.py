import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080))
server.listen(5)

def startServer():
    global server
    while True:
        client, address = server.accept()
        print(f"Connected to {address}")
        wholeData = ""
        while True:
            data = client.recv(1024)
            if not data:
                break
            wholeData += data.decode('utf-8')
            print(f"Received data: {data.decode('utf-8')}")
            # client.send(data)
        print(f"Received all data: {wholeData}")
        #open file and ovwerwrite it
        with open("recievedData.txt", "w") as f:
            f.write(wholeData)


threading.Thread(target=startServer, daemon=True).start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Closing server")
    server.close()
    



