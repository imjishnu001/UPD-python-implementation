import socket
import csv

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #Socket Object UPD
address = ("127.0.0.1",5002)                             #Incomming channel
sock.bind(address)                                       #Binding socket with incomming channel



def getFullInfo(extNum,addr,i,csv_data):
    '''
    Function to fetch and send all information using id
    '''
    for row in csv_data:                #Ittrating through csv file
        if extNum == row[3]:            #Matchin search string with csv data
            i = i+1                     #Flag to identify no match
            sock.sendto(bytes(str("\nName: "+row[0]+"\nEmail: "+row[1]+"\nBatch: "+row[2]),"utf-8"),addr)  #Sending response to client
    if i == 0:                          #No match found
        sock.sendto(bytes(str("No record found"),"utf-8"),addr) #Sending response to client   

def getNameId(rank,addr,i,csv_data):
    '''
    Function to fetch and send name and ID using Batch
    '''
    for row in csv_data:                                        #Ittrating through csv file
        if sorted(rank) == sorted(row[2]):                      #Matchin search string with csv data
            i += 1                                              #Flag to identify no match    
            searchResullt.append([row[0],row[3]])               #Appending matching data to list 
    sock.sendto(bytes(str(searchResullt),"utf-8"),addr)         #Sending response to client
    if i == 0:                          #No match found                
        sock.sendto(bytes(str("No record found"),"utf-8"),addr) #Sending response to client
    searchResullt.clear()
    

while True:
    i=0                              
    searchResullt = []
    csv_data = csv.reader(open('csv.csv','r'))  #Loading csv file
    data,addr = sock.recvfrom(1024)             #Setting max buffer size for incoming data 
    decodedData = data.decode("utf-8")          #Decoding bytes to string
    choice = decodedData[-1:]                   #Extracting user choice from decoded string        
    search = decodedData[:-1]                   #Extracting  from decoded string
    
    
    print(f'Connection established with{addr}')

    #Calling function based on user choice 
    if int(choice) == 1:
        getFullInfo(search,addr,i,csv_data)        #User Function call for full information
    elif int(choice) == 2:
        getNameId(search,addr,i,csv_data)            #User Function call
    
