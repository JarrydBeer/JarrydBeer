#8064413 Jarryd Beer Version 5 IP range ping sweep.
#using the subprocess library to ping IP addresses and using the TTL result from the ping to verify if the address is alive
import subprocess
import re
print("Welcome to Ping Sweeper\nPlease follow instructions to begin your search\nYou will be required to enter IP addresses in the following format\nxxx.xxx.xxx.xxx")

First_ip = input("Enter the First IP Address ")                         #Ip address to begin Scan
Last_ip = input("Enter the Last IP Address ")                           #Ip address to end Scan

def Get_Host(x):                                                        #defining Get_Host as a function
    Dot_Count = 0                                                       #There are 3 '.' in an IP (eg 192.168.0.1) to seperate the information the client is going to give us. 
    Pos_Count = 0
    for i in x:                                                         #For what we're going to recieve from the client
        if i == ".":        
            Dot_Count = Dot_Count + 1                                   #Everytime the client recieves a dot we're going to add a count
        if Dot_Count == 3:                                              #Once the count == 3, x will be returned, as we don't need anymore dots.
            return(x[0:Pos_Count +1], x[Pos_Count+1: ])                 #Once x is returned it will be from the first position in the IP Address until the end of the string
            break       
        Pos_Count += 1                                                  #increases dot count varibale by 1

Network, First_Host = Get_Host(First_ip)
Network, Last_Host = Get_Host(Last_ip)                                  #Calls first 

Empty_String = ""
Counter = 0

for ip in range(int(First_Host),int(Last_Host) +1):                     #For loop, For every ip in the range from first host to last host. Need to add one to cover python ending result one position early
    Process = subprocess.getoutput("ping -n 1 " + Network + str(ip))    #calling the subprocess library, -n is windows, 1 is how many pings we want to send, concantonating with the network variable above & the IP address.
    Empty_String += Process                                             #Result from the ping will give (Request timed out) or (Reply from xxx.xxx.x.x ping TTL)
    String_needed = re.compile(r"TTL=")                                 #(r)ow is for whatever i want to look for it will look for it. This gives us the ability to search the ping result.
    mo = String_needed.search(Empty_String)                             #Points the above command to search the emppty string variable created
    try:                                                                #attempted try/except instead of for/while loop to avoid errors
        if mo.group() == 'TTL=':            
            print("Host " + Network + str(ip) + " is alive")
    except:
        print("Host " + Network + str(ip) + " is dead")                 #What these will do is the program will try to search in the ping results for TTL. If it is able to find it will print the Host, 

    Empty_String = ""    
print('Search Completed')

#https://youtu.be/iqtZm5w_V2c (Uploaded without Volume, use below link)
#https://youtu.be/n-GYWp-vi_E
