from curses.ascii import isupper
from importlib.metadata import files
import socket


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

import os
ip="127.0.0.1"
port =4503
server_soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_soc.bind((ip,port))
server_soc.listen(10)

while True:
    client_soc,address=server_soc.accept()
    print("Connected at  :",address[0],"  ",address[1])
    request_inp=client_soc.recv(1024)
    request_inp=request_inp.decode('utf-8')
    
    #request_inp=caesar(request_inp,26-shift)
    request_inp=request_inp[::-1]
    #request_inp=request_inp
    
    
    print("REQUESTED COMMAND :",request_inp)
    if request_inp=='cwd':
        print(os. getcwd())

        #client_soc.send(caesar(os. getcwd(),shift).encode('utf-8'))
        client_soc.send(os. getcwd()[::-1].encode('utf-8'))
        #client_soc.send(os. getcwd().encode('utf-8'))

    elif request_inp=='ls':
        print(os.listdir())
        list=[x for x in os.listdir()]
        list=str(list)

        #client_soc.send(caesar(list,shift).encode('utf-8'))
        client_soc.send(list[::-1].encode('utf-8'))

    elif request_inp[0:2]=='cd':
        
        status="OK"
        try:
            #print()
            os.chdir(request_inp[3:])
        except:
            status= "NOT OK"
        msg=request_inp +"   STATUS: "+status

        #client_soc.send(caesar(msg,shift).encode('utf-8'))
        client_soc.send(msg[::-1].encode('utf-8'))

    elif request_inp[0:3]=='upd':
        file_name=request_inp[4:]
        base_name=os.path.basename(file_name)
        file=open("uploaded.txt","w")
        print("file name we recieve :" ,file_name)
        name_recieved="We recieved filename :"+base_name
        client_soc.send(name_recieved.encode('utf-8'))
        
        data=client_soc.recv(1024).decode('utf-8')

        #data=caesar(data,26-shift)
        data=data[::-1]

        if(data!="File does not exists"):
            file.write(data)
            file.close()
            status="STATUS :OK"

            #client_soc.send(caesar(status,shift).encode('utf-8'))
            client_soc.send(status[::-1].encode('utf-8'))

        else:
            file.close()

            status="STATUS :NOT OK"
            print(status)
            
            #client_soc.send(caesar(status,shift).encode('utf-8'))
            client_soc.send(status[::-1].encode('utf-8'))

    elif request_inp[0:3]=='dwd':
        file_name=request_inp[4:]
        try:
            file=open(file_name,"r")
            data=file.read()

            #client_soc.send(caesar(data,shift).encode('utf-8'))
            client_soc.send(data[::-1].encode('utf-8'))
            #server_soc.send(data.encode('utf-8'))
        except:
            not_exist="File does not exists"
            #server_soc.send(not_exist.encode('utf-8'))
            data=not_exist

            #client_soc.send(caesar(data,shift).encode('utf-8'))
            client_soc.send(data[::-1].encode('utf-8'))

        ##client_soc.send(data.encode('utf-8'))





    
    ##client_soc.send(request_inp.upper().encode('utf-8'))

    client_soc.close()

