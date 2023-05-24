# UDP Server
from socket import *

def prime_checker(num):
   try:
        num=int(num)
   except:
        prime_flag=-1
        return str(prime_flag)
   if num>1:
        prime_flag=1
        for i in range(2,num):
            if (num%i)==0:
                prime_flag=0
                break
   else :
        prime_flag= 0
   return str(prime_flag)
serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Server ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Datagram from:", clientAddress)
    message = message.decode('utf-8')
    isprime=prime_checker(message)
    serverSocket.sendto(isprime.encode('utf-8'), clientAddress)
    
# UDP Client
from socket import *
serverName = 'localhost'
serverPort=12000
clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(10)
message=input('Insert a number:')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
try:
    isprime, serverAddress = clientSocket.recvfrom(2048)
    isprime=isprime.decode('utf-8')
    if isprime=="1":
        print("It's a prime number")
    elif isprime=="0":
        print("It is not a prime number")
    else :
        print("Incorrect entry")
except:
    print("Timeout")
finally:
    clientSocket.close()
