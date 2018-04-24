#!/usr/bin/env python
#encoding:utf-8

from config import settings

from Crypto.Cipher import AES
def encrypt(message):
    key=settings.DATA_KEY  #由用户输入的16位或24位或32位长的初始密码字符串
    cipher=AES.new(key,AES.MODE_CBC,key)
    ba_data=bytearray(message,encoding='utf-8')  #ba_data必须是16字节或16字节的倍数
    v1=len(ba_data)
    v2=v1 % 16
    if v2==0:
        v3=16
    else:
        v3=16-v2
    for i in range(v3):  #填充相差的字节数，以满足16或者16的倍数
        ba_data.append(v3)
    final_data=ba_data.decode('utf-8')
    msg=cipher.encrypt(final_data)
    return msg


def decrypt(msg):
    key = settings.DATA_KEY
    cipher=AES.new(key,AES.MODE_CBC,key)
    result=cipher.decrypt(msg)
    data=result[0:-result[-1]]  #去除填充的数据
    return str(data,encoding='utf-8')

def auth():
    import hashlib
    import time
    key='dfjiosajiofjewnenwoiewfndsslafdsa'

    ctime=time.time()
    m=hashlib.md5()
    new_key="%s|%s"%(key,ctime)
    m.update(new_key.encode("utf8"))
    md5_key=m.hexdigest()
    md5_time_key="%s|%s" %(md5_key,ctime)
    return md5_time_key
