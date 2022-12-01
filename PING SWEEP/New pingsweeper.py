from pythonping import ping




nr_of_ips = int(input("How many ip addresses do you want to ping? "))
ip_addresses = []

for i in range(nr_of_ips):
    ip_address = input("Enter an IP address: ")
    ip_addresses.append(ip_address)

print("")

for x in ip_addresses:
    print(f"Result for : {x}")
    ping(x, verbose=True, count=2)
    print("")
       