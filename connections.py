import paramiko
import MySQLdb
import sys


# Pseudocode

def SSH_Conn():
    "SSH into Koding machine. Changes the port?"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('vm-0.carolus4.koding.kd.io', username='carolus4', password = 'pipipi')

def MySQL_Conn():
    "Connect to development database."
    conn = ()
    return conn

def input():
    f = open('', 'r')
    return f

def output(content):
    database.write(content)