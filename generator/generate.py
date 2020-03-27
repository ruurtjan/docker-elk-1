import time
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("logstash",5000))

while True:
    byt="{\"cpu\": 3.3, \"memory\": 123, \"memory_size\": 1024, \"msg\": \"hello world!\"}\n".encode()
    s.sendall(byt)
    time.sleep(1)