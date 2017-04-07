#!/usr/bin/python
# -*- coding: utf-8 -*-

from paramiko.client import SSHClient

import paramiko
help (paramiko.client)
sys.exit()
client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '192.168.202.10'
user = 'noturno'
passwd = '4linux'


client.connect(hostname=host, username=user, password=passwd)


stdin,stdout,stderr = client.exec_command('ls -la /')
print stdout.read()

if stderr.channel.recv_exit_status() !=0:
	print stderr.channel.recv_exit_status()
	print stderr.read()

else

print stdout.read()