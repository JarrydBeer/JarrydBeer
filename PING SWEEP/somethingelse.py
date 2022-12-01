import platform
import os

print("""
1.Enter an IP range for the ping sweep.
2.Enter the first address to ping
3.Enter the last address to ping

    Example: 192.168.56
             1   
             15
This will scan Ip Address 192.168.56.1 through 192.168.56.15 \n""")        

user_input = input('Enter the network IP: ')

ip_parts = user_input.split('.')
network_ip = ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.'

first_host = int(input("Enter the First number: "))
last_host = int(input("Enter the Last number: "))
last_host += 1

oper = platform.system

if (oper == "Windows"):
    ping = "ping -n 1 "
else:
    ping = "ping -c 1 "

print("Scanning in Progress")

for ip in range(first_host,last_host):
    addr = network_ip + str(ip)
    command = ping + addr
    response = os.popen(command)
    list = response.readlines()
    


    for line in list:
        if(line.count("TTL")):
            print(addr, "--> Alive")
            break


print("Scanning complete")
