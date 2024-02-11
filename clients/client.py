import socket
import json

UDP_IP = "192.168.1.9"
UDP_PORT = 1509

#connection string
message = json.dumps({"type":"c","uniqueid":"bcd123","os":"windows","name":"xv"})

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
print(f"Message sent to {UDP_IP}:{UDP_PORT}")

try:
    message,address = sock.recvfrom(1024)
    jsonMsg = json.loads(message.decode())
    reply = json.dumps({"type":"r","data":"hello mtf!","to":jsonMsg['to']})
    sock.sendto(reply.encode(), (UDP_IP, UDP_PORT))
    print(jsonMsg['cmd'])
    # print(f" commmand is {jsonMsg["cmd"]}")
    # print(f" sending back to  {jsonMsg["to"]}")

finally:
    sock.close()
