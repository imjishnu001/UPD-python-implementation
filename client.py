import socket
import time
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Socket Object UPD

def search(search,choice):
    '''
    search function send user input,
    search string and user choice to server
    '''
    addr = ("127.0.0.1",5002)                           #Server details
    sock.sendto(bytes(search+str(choice),"utf-8"),addr) #Sending search string and user choice to server
    getResponse(choice)                                 #Function call to display server response

def getResponse(choice):
    '''
    getResponse function receives and decodes
    the response sent by server
    '''
    try:
        if choice == 2:                                                     #Receiving multiple data
            data,addr = sock.recvfrom(10000)                                #Setting max buffer size
            stringData = bytearray(data).decode('utf-8')                    #Decoding bytes to string
            modifiedData = stringData.replace("[", "\n")                    #Adding new lines
            modifiedData = re.sub('[^A-Za-z0-9\n@., ]+', '', modifiedData)  #Striping unused characters
            print(modifiedData,'.')                                         #Display final list
        else:    
            data,addr = sock.recvfrom(10000)                                #Setting max buffer size
            print(data.decode())                                            #Display decoded response
    except:
        print("No response from server")

 
quit = 0
while quit==0:
    #User selection options 
    print("\n\n\n1. Full information")
    print("2. Name and Id(using batch)")
    print("3. Quit")
    try:
        choice = int(input("\nEnter a number: "))      #Input to select desired option
    except:
        print("Please Enter a number")                 #Invalid selection
        continue
    if choice == 1:
        extNum = input("\nID: ")                 #Search string
        search(extNum,choice)                          #Search function call
    elif choice == 2:
        rank = input("\nBatch: ")                        #Search string
        search(rank,choice)                             #Search function call
    elif choice == 3:
        quit=1                                          
        print("Good bye")                               #Program termination 
    else:
        print("Invalid selection")                      #Invalid user selection
    


 
