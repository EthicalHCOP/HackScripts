import socket
import os

resultados = open('resultados.txt', 'w')
port_list=[21, 22, 23, 25, 53, 80, 88, 110, 111, 135, 139, 143, 389, 443, 445, 587, 636, 993, 1433, 2049, 3268, 3269, 3306, 3389, 5060, 5061, 5900, 5985, 5986, 6666, 7777, 8000, 8080, 8081, 8089, 8888]

def escanearIPs():
    fpingc = os.popen('fping -a -g [RANGO_IP] 2>/dev/null')
    salida = fpingc.read()
    listaIPS = salida.split()
    log("*___ Lista de Direcciones IP ___* \n"+salida+"\n")
    return listaIPS

def escaner (ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not sock.connect_ex((ip, port)):
        log("El puerto " + str(port) + "/tcp esta abierto")

def main():
    listaIPS = escanearIPs()
    for ip in listaIPS:
        log("*____ IP: "+ip+" ____*")
        for port in port_list:
            escaner(ip, port)

def log(txt):
    print(txt)
    resultados.write(txt+"\n")

if __name__ == "__main__":
    main()
