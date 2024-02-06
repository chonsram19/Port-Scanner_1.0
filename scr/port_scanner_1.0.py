#!/bin/python3

import sys
import socket
from datetime import datetime

#Define target

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
else:
        print("Invalid amount of arguments.")
        print("Syntax: scanner.py <ip>.")


print("_" * 60)

print("Scanning target: " + target)
print("Time Started " + str(datetime.now()))
print("-" * 60)

try:
       for port in range(1, 100):
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             socket.setdefaulttimeout(1)
             result = s.connect_ex((target, port))
             
             if(result == 0 ):
                 print(f"Port {port} is open")
             s.close()
except KeyboardInterrupt:
       print("\nExciting Progam")
       sys.exit()

except socket.gaierror:
       print("Hostname could not be resolved")
       sys.exit()
except socket.error:
       print("Could not connect to the server")
       sys.exit()

