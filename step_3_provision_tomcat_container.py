#!/usr/bin/env python
import os
import subprocess
import time

os.system('figlet -w 120 -f standard "Provision Tomcat"')

os.system('figlet -w 120 -f slant "Building war"')

os.system('mvn -q clean compile war:war')

os.system('figlet -w 120 -f slant "Creating configuration"')

file = open("oracleConfig.properties", "w")
file.write("url=jdbc:oracle:thin:@oracle:1521/xe"+ os.linesep)
file.write("user=system"+ os.linesep)
file.write("password=oracle"+ os.linesep)
file.close()

os.system('docker cp oracleConfig.properties tomcat:/usr/local/tomcat/webapps/oracleConfig.properties')

os.system('figlet -w 120 -f slant "Deploying Application"')

os.system('docker cp target/passwordAPI.war tomcat:/usr/local/tomcat/webapps/passwordAPI.war')

os.system('docker logs tomcat 2> temp >/dev/null')
process = subprocess.Popen(["grep","-c","Deployment of web application archive \[/usr/local/tomcat/webapps/passwordAPI.war\] has finished","temp"], stdout=subprocess.PIPE)
deploys_starting = int(process.stdout.read().decode('utf-8'))

ready = False
while not ready:
    os.system('docker logs tomcat 2> temp >/dev/null')
    process = subprocess.Popen(["grep","-c","Deployment of web application archive \[/usr/local/tomcat/webapps/passwordAPI.war\] has finished","temp"], stdout=subprocess.PIPE)
    deploys_now = int(process.stdout.read().decode('utf-8'))
    ready = deploys_now > deploys_starting
    time.sleep(1)

os.system('rm oracleConfig.properties temp')