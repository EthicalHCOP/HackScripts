#!/usr/bin/env python3

import sys
import base64

def help():
    print("Returns PowerShell base64 encoded cmdline payload")
    exit()

payload = ''
cmdline = "powershell -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print(cmdline)
