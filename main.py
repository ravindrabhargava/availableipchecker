import ipaddress

def read_used_ips(file_path):
    with open(file_path, "r") as file:
        used_ips = [line.strip() for line in file.readlines()]
    return used_ips

def write_available_ips(file_path, available_ips):
    with open(file_path, "w") as file:
        for ip in available_ips:
            file.write(ip + "\n")

def find_available_ips(subnet, used_ips):
    network = ipaddress.ip_network(subnet)
    available_ips = []
    for ip in network:
        if str(ip) not in used_ips:
            available_ips.append(str(ip))
    return available_ips

# Main program execution
if __name__ == "__main__":
    subnet = "192.168.0.0/16"
    used_ips_file = "usedfile.txt"
    available_ips_file = "available-ips.txt"

    used_ips = read_used_ips(used_ips_file)
    available_ips = find_available_ips(subnet, used_ips)

    if available_ips:
        write_available_ips(available_ips_file, available_ips)
        print("Available IPs in subnet {} written to {}".format(subnet, available_ips_file))
    else:
        print("No available IPs found in subnet {}".format(subnet))