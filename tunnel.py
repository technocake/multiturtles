#coding: utf-8
import socket
import struct
import threading

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 1337



# setting up transmitter socket for sending commands from self program
transmitter = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
transmitter.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

def gi_beskjed(hvem, hva, hvor):
    msg = "%s,%s,%s,%s\n"%(hvem ,hva ,hvor[0],hvor[1])
    #buffer = bytes(msg)
    transmitter.sendto(msg, (MCAST_GRP, MCAST_PORT))
    print(hvem,hva,hvor)


# set up receiving socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
                             # to MCAST_GRP, not all groups on MCAST_PORT
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

targetturtle = None

def lytt():
    global targetturtle
    print('Listening thread started with turtle target', targetturtle)
    while True:
        buffer = sock.recv(10240)
        amsg = str(buffer).rstrip()
        liste = amsg.split(',')
        if len(liste) == 4:
            hvem = liste[0]
            hva  = liste[1]
            hvor = [float(liste[2]), float(liste[3])]
            print(hvem, hva, hvor)
            if targetturtle != None:
                targetturtle(hvem, hva, hvor)

def init(target):
    global targetturtle
    targetturtle = target
    t = threading.Thread(target=lytt)
    t.daemon = True
    t.start()

def spacekey():
    gi_beskjed('donaldino', 'goto', '0,0')

if __name__ == '__main__':
    import turtle
    init(turtle) # self init...

    turtle.onkey(spacekey, 'space')
    turtle.listen()
    turtle.mainloop()
