
from fileinput import filename
import socket
from urllib import request
import os
shift=4
def caesar(text,s):
    result = ""
  
    for i in range(len(text)):
        char = text[i]
  
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
  
        elif(char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=char
  
    return result


ip="127.0.0.1"
port =4503
while True:
    server_soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_soc.connect((ip,port))
    request_inp=input("put the command:  ")
    # print("~~~~~~~~~~~~")
    # cae_encrypt=caesar(request_inp,shift)
    # print(cae_encrypt)
    # print(caesar(cae_encrypt,26-shift))
    # print('~~~~~~~~~~~~')
  
    #server_soc.send(caesar(request_inp,shift).encode("'utf-8"))
    server_soc.send(request_inp[::-1].encode("'utf-8"))
    #server_soc.send(request_inp.encode("'utf-8"))

    recieved=server_soc.recv(1024)
    recieved=recieved.decode('utf-8')

    #recieved=caesar(recieved,26-shift)
    recieved=recieved[::-1]
    
    #print("RECIEVED", recieved)
    if request_inp=='cwd':
        print("Recieve :", recieved)
    if request_inp=='ls':
        print("Recieve :", recieved)
    if request_inp[0:2]=='cd':
        print("Recieve :", recieved)  
        #print("Recieve :", recieved) 
    if request_inp[0:3]=='upd':
        file_name=request_inp[4:]
        try:
            file=open(file_name,"r")
            data=file.read()
            #server_soc.send(data.encode('utf-8'))
        except:
            not_exist="File does not exists"
            #server_soc.send(not_exist.encode('utf-8'))
            data=not_exist

        #server_soc.send(caesar(data,shift).encode('utf-8'))
        server_soc.send(data[::-1].encode('utf-8'))

        status_recieved=server_soc.recv(1024)

        #print(caesar(status_recieved.decode('utf-8'),-shift))
        print(status_recieved.decode('utf-8')[::-1])

    if request_inp[0:3]=='dwd':
        file_name=request_inp[4:]
        base_name=os.path.basename(file_name)
        file=open("downloaded.txt","w")
        print("file name we recieve :" ,file_name)
        # name_recieved="We recieved filename :"+base_name
        # server_soc.send(name_recieved.encode('utf-8'))
        # data=server_soc.recv(1024).decode('utf-8')
        #print(caesar(recieved,shift),"     Haaaaaaaaaaaaaaaaaad")
        #recieved=caesar(recieved,shift)
        #print(recieved, "   JFIDWIFAKJ")
        if(recieved!="File does not exists"):
            
            file.write(recieved)
            file.close()
            status="STATUS :OK"
            print(status)
            ##client_soc.send(status.encode('utf-8'))
        else:
            file.close()
            os.remove("downloaded.txt")

            status="STATUS :NOT OK"
            print(status)
            
            server_soc.send(status.encode('utf-8'))
    else:
        #print("RECIEVED", caesar(recieved,-shift))
        continue

        #print(status_recieved.decode('utf-8'))









