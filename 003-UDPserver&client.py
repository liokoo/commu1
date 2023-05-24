# UDP Server
from socket import *
serverPort=12000
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('Ready to receive')
vowels = ['A','E','I','O','U']
          
while 1:
    message, clientAddress=serverSocket.recvfrom(2048)
    message=message.decode('utf-8')
    num=len(message)
    for voc in vowels:
          num =num–message.count(voc)
          answer = "Message has "+str(num)+"consonants."
          serverSocket.sendto(answer.encode('utf-8'), clientAddress)
          
# UDP Client
from socket import *
serverPort=12000
clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)
          
message = input('Insert a word (without special characters):') 
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
          
try:
      reply, serverAddress = clientSocket.recvfrom(2048)
      print(reply.decode('utf-8'))
expect:
      print("Timeout, the server did not respond in time")
finally:   
      clientSocket.close()
