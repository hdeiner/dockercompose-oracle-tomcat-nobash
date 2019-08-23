#!/usr/bin/env python
import os
import subprocess

os.system('figlet -w 120 -f standard "Provision Oracle"')

os.system('figlet -w 120 -f slant "Running Liquibase"')

file = open("liquibase.properties", "w")
file.write("driver: oracle.jdbc.driver.OracleDriver"+ os.linesep)
file.write("classpath: lib/ojdbc6.jar"+ os.linesep)
file.write("url: jdbc:oracle:thin:@localhost:1521:xe"+ os.linesep)
file.write("username: system"+ os.linesep)
file.write("password: oracle"+ os.linesep)
file.close()

os.system('liquibase --changeLogFile=src/main/db/changelog.xml update')

os.system('rm liquibase.properties')



