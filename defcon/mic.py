import socket
import time

# AF_INET for IPv4, SOCK_STREAM for TCP (as opposed to UDP).
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket what IP and port number to connect to (must be in two brackets because it needs a tuple).
clientSocket.connect(('simple-service-c45xrrmhuc5su.shellweplayaga.me', 31337))
print('>> Connected')

# Recieve 1024 bytes of data.
data = clientSocket.recv(1024)
print ('>> data received: ',data.decode("utf-8"))

# Team Ticket
ticket = b'ticket{SternPier7063n22:RJju2dYLPdjH75iLo3X_SLntCBciH65TCoY_JxtOcLSKRRdf}\r\n'
print(">> Ticket is: ",ticket)
#byticket = bytes(ticket,'UTF-8')

# Send ticket
print('>> Sending ticket...')
clientSocket.send(ticket)
#time.sleep(2)
#clientSocket.send(ticket)
print('>> Ticket sent.')

#Split the recieved data by newlines (returns a list).
#data = data.split('\n')

#The first and second elements in our list should be the two numbers we need to add together, so we do that.
#result = int(data[0]) + int(data[1])

#Send our result to the server.
#clientsocket.send(str(result))

# Recieve any response from the server and print it to the screen.
data = clientSocket.recv(1024)
print(">> Second data: ",data)

result = data.decode('utf-8')
print(">> data as string called result: ",result)

resultArr = result.split(' +')
num1 = resultArr[0]

num2 = filter(str.isdigit,resultArr[1])
num2 = "".join(num2)

output = int(num1) + int(num2)
outputB = str(output) + "\n"
outputB = outputB.encode()

clientSocket.send(outputB)

#result = result.split(' +')
#print(">> ",result[0])

#num1 = filter(str.isdigit, result[0])
#num1str = "".join(num1)
#print(">> num1: ",num1str)

#num2 = filter(str.isdigit, result[1])
#num2str = "".join(num2)
#print(">> num2: ",num2str)

#numSum = int(num1str) + int(num2str)
#print("numSum = ",numSum)

#numToSend = str(numSum) + "\n"
#clientSocket.send(numToSend.encode())

data = clientSocket.recv(1024)
print("Received: ",data)

#data = bytes(data.split(' +'),'utf-8')
#print(data[0])
#result = bytes((int(data[0]) + int(data[1]) + '\n'),'utf-8')
#clientSocket.send(result)

clientSocket.close()

