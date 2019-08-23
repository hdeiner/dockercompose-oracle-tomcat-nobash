#!/usr/bin/env python
import os
import subprocess
import time

os.system('figlet -w 120 -f standard "Run Tests"')

process = subprocess.Popen(["curl","-s","http://localhost:8080/passwordAPI/passwordDB","temp"], stdout=subprocess.PIPE)
output = process.stdout.read().decode('utf-8')
if ('RESULT_SET' in output):
    os.system('figlet -w 120 -f slant "Smoke Test Success"')
    file = open("rest_webservice.properties", "w")
    file.write("hosturl=http://localhost:8080"+ os.linesep)
    file.close()
    os.system('mvn -q verify failsafe:integration-test')
else:
    os.system('figlet -w 120 -f slant "Smoke Test Failure"')

os.system('rm rest_webservice.properties temp')