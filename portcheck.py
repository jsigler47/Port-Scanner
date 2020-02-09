import socket
import subprocess
import sys
from datetime import datetime
from threading import Thread

#Built from code snippet below
#https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
def scan_ports(remoteServerIP,port):
    '''
    Args:
        remoteServerIP (str): Address of server to check port status on.
        port (int): port to check the status of on remoteServerIP
    Returns:
        None. Prints message for open ports only.
    '''
    #Scan ports 1-1024
    try:
        #Create a new socket using AF_INET family and socket type of SOCK_STREAM
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Attempt connection to the remote server's specified port with sock
        result=sock.connect_ex((remoteServerIP,port))
        if result == 0:
            #No error and connected, port is open.
            print(f'Port {port}: Open')
        sock.close()

    except KeyboardInterrupt:
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved.')
        sys.exit()

    except socket.error:
        print('Could not connect to server')
        sys.exit()

    
#Clear screen
subprocess.call('clear', shell=True)

network_to_scan = '192.168.1.'
#TODO: Add command line argument options for network_to_scan and print to file.

t1 = datetime.now()
#Scan entire network
for ip in range(0,255):
    server_to_scan = network_to_scan+str(ip)
    remoteServerIP = socket.gethostbyname(server_to_scan)
    threads = []
    
    #Thread the port scanning.
    try:
        socket.gethostbyaddr(remoteServerIP)
        
        print('-'*60)
        print(f'Scanning remote host: {server_to_scan}')
        print('-'*60)
        
        for port in range(1,1025):
            process = Thread(target=scan_ports, args=[remoteServerIP,port])
            process.start()
            threads.append(process)
            
        #Join all threads
        for process in threads:
            process.join()
            
    except socket.herror:
        print('-'*60)
        print(f'No host at {remoteServerIP}')
        print('-'*60)
    
t2 = datetime.now()
total_time = t2-t1
print(f'Scan complted in: {total_time}')
