import socket

def scan_ports(ip):
    open_ports = []
    for port in range(1, 1025):
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports
