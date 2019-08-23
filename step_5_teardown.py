#!/usr/bin/env python
import os

os.system('figlet -w 120 -f standard "Destroy Oracle and Tomcat Containers"')
os.system('docker-compose -f dockercompose-incentives-integration-testing.yml down')