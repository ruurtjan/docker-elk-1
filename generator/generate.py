import time
import socket
import random

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("logstash",5000))

cpu_spike = 0
mem_spike = 0
while True:
    
    if cpu_spike > 0:
        cpu = random.randrange(800, 999) / 10
    else:
        if random.randrange(60) < 1:
            cpu_spike = random.randrange(5,15)
        cpu = random.randrange(10, 50) / 10
    
    if mem_spike > 0:
        mem = random.randrange(900, 950)
    else:
        if random.randrange(60) < 1:
            mem_spike = random.randrange(5,15)
        mem = random.randrange(120, 123)

    
    byt = f"{{\"cpu\": {cpu}, \"memory\": {mem}, \"memory_size\": 1024}}\n".encode()
    s.sendall(byt)

    for _ in range(random.randrange(1,7)):
        p = random.randrange(60)
        if p < 1:
            resp = 500
        elif p < 4:
            resp = 404
        else:
            resp = 200

        latency = random.randrange(5,15)
        class_id = random.randrange(1,5)

        byt = f"{{ \"response_code\": {resp}, \"latency_ms\": {latency}, \"class\": {class_id}}}\n".encode()
        s.sendall(byt)

    cpu_spike = cpu_spike - 1
    mem_spike = mem_spike - 1
    time.sleep(1)
