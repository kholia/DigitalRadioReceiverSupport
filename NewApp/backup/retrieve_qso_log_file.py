#!/usr/bin/env python3

import sys
import subprocess

from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

# Load the public and private keys
adbkey = 'adbkey'
with open(adbkey) as f:
    priv = f.read()
with open(adbkey + '.pub') as f:
     pub = f.read()
signer = PythonRSASigner(pub, priv)

# Connect
device1 = AdbDeviceTcp(sys.argv[1], 5555, default_transport_timeout_s=9.)
device1.connect(rsa_keys=[signer], auth_timeout_s=0.1)

response1 = device1.root()
response1 = device1.shell('cp /data/data/com.bunzee.ft8radio/files/qso_logs.txt /data/local/tmp; chmod 777 /data/local/tmp/qso_logs.txt')

subprocess.run(["adb", "pull", "/data/local/tmp/qso_logs.txt", "."])
