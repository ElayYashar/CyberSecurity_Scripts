import os
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enters the the IP after the file name 
IP = argv[1]
SSH = 22
target_ip = socket.gethostbyname(IP)
# Enters the ports after the IP
ports = [argv[2] ,argv[3] ,argv[4]]

def knock(arr):
    for p in ports:
        os.system("ping -n 1 " + str(IP) + " | findstr Received") # os.system("telnet " + str(IP) + " " + str(p))

def scanPort(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

def isHostUp(ip):
    response = os.popen(f"ping -n 1 -w 2 " + ip).read()
    if "Received = 1" in response:
        return True
    return False

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def possiblePermutations(arr, index):
    if scanPort(SSH) == True:
        print("[+] SSH is up\nCorrent Squence: ")
        print(arr)
        return
    
    if index == 1:
        print(arr)
        knock(arr)
    else:
        for i in range(index - 1):
            possiblePermutations(arr, index -1)

            if(index % 2 == 0):
                swap(arr, i, index - 1)
            else:
                swap(arr, 0, index -1)
        
        possiblePermutations(arr, index - 1)

if(isHostUp(target_ip)):
    print("[+] Scanning "  + target_ip + "...") # Check if host is up and can be scanned

    possiblePermutations(ports, len(ports))
    
else:
    print("Host Is Not Up!")

print(scanPort(SSH))
