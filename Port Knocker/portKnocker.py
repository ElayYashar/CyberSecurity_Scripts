import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "10.0.0.17"
SSH = 22
target_ip = socket.gethostbyname(IP)
ports = [10000 ,4444 ,65535]

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