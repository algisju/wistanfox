import nmap
nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP address to scan: ")
    if not ip:
        break
    print(f"\n--- beginning scan of {ip}")
    output = nm.scan(ip, '22-1024')
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output -------------------")
    print(output)
