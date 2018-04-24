#!/usr/bin/env python
#encoding:utf-8
# import subprocess
# v=subprocess.getoutput("ipconfig")
# print(v[150:200])

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.199', port=22, username='root', password='lchd1234')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ip a')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()

print(result)