import socket #library to allo connections

s = socket.socket() #initialize socket
host = socket.gethostname() #get host address of program (which client.py will connect to)
port = 8080
s.bind((host,port)) #bind socket to host and port
s.listen(1) #listen for one computer

print(host)
print('waiting for any incoming connections...')

conn, addre = s.accept() #accept connections

print(addre, 'Has connected to the server')

filename = input(str('Please enter the filename of the file: '))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully.")
