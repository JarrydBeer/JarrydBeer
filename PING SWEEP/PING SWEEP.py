import subprocess
import ipaddress

IP_address = input("Please enter a beginning IPv4 address start sweep(ex.192.168.56.0/20): ")   #Assigns variable to IP_address to as a value for user to input starting IP address
ip_net = ipaddress.ip_network(IP_address)   #assigns variable to ip_net to the library ipaddress. The library allows for the ping/manipulation of IPv4/IPv6 address's 
all_hosts = list(ip_net.hosts())   #Search for all hosts on the network

for i in range(len(all_hosts)): 
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0] #for each IP on the subnet run the ping command with the subprocess.poppen library
    
    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(all_hosts[i]), "Is Dead")
    elif "Request timed out" in output.decode('utf-8'):
        print(str(all_hosts[i]), "Is Dead")
    else:
        print(str(all_hosts[i]), "Is Alive")



