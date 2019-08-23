#!/usr/bin/env python
import os
import subprocess
import time

os.system('figlet -w 120 -f standard "Create Oracle and Tomcat Containers"')
os.system('docker-compose -f dockercompose-incentives-integration-testing.yml up -d')

print("waiting for Oracle to start")
ready = False
while not ready:
    process = subprocess.Popen(["curl","-s","localhost:8081"], stdout=subprocess.PIPE)
    output = process.stdout.read()
    ready = "DOCTYPE HTML PUBLIC" in output.decode('utf-8')
    time.sleep(1)

print("waiting for Tomcat to start")
ready = False
while not ready:
    process = subprocess.Popen(["curl","-s","localhost:8080"], stdout=subprocess.PIPE)
    output = process.stdout.read()
    ready = "Apache Tomcat" in output.decode('utf-8')
    time.sleep(1)
