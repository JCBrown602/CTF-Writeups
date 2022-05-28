# DEFCON 30 - mic_check_1 - Team PFAATX
# Python socket code
import socket

# AF_INET for IPv4, SOCK_STREAM for TCP (as opposed to UDP).
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket what IP and port number to connect to 
#(must be in two brackets because it needs a tuple).
clientSocket.connect(('simple-service-c45xrrmhuc5su.shellweplayaga.me', 31337))
print('>> Connected')

# Recieve 1024 bytes of data.
data = clientSocket.recv(1024)
print ('>> Data received: ',data.decode("utf-8"))

# Team Ticket
ticket = b'ticket{SternPier7063n22:RJju2dYLPdjH75iLo3X_SLntCBciH65TCoY_JxtOcLSKRRdf}\r\n'
print(">> Ticket is: ",ticket)

# Send ticket
print('>> Sending ticket...')
clientSocket.send(ticket)
print('>> Ticket sent.')

# Receive response from the server and print it to the screen.
data = clientSocket.recv(1024)
print(">> Solve this: ",data)

# Response is in bytes so convert it to a string
result = data.decode('utf-8')
print(">> Problem as string called result: ",result)

# Split the string at the '+' so we have the two sides of the equation
resultArr = result.split(' +')
# First half
num1 = resultArr[0]
# Second half: remove anything not a digit
num2 = filter(str.isdigit,resultArr[1])
# Filter makes an array so put the elements back together
num2 = "".join(num2)

# Do the math, casting to int's
output = int(num1) + int(num2)
# Have to convert to string to get to bytes (only way I know atm)
outputB = str(output) + "\n"
# Convert to bytes
outputB = outputB.encode()

# Send solution to the server
clientSocket.send(outputB)

# We need the response to know if it's right and to get the flag
data = clientSocket.recv(1024)
print("Received: ",data)

# Let's be nice and close the socket
clientSocket.close()

