#!/usr/bin/env python
#coding:utf-8
from Course_system.lib import Open_file
class login():
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def login_func(self):
        userdata=Open_file.Open_file_class()
        read_file=userdata.read()
        if self.username in read_file and read_file[self.username].get('password') :
            if self.password==read_file[self.username]['password']:
                if not read_file[self.username]['login']:
                    read_file[self.username]['login']=True
                    print('login successfully')
                flag=True
                return read_file[self.username]

            else:
                print('password error,please re-enter')

        else:
            print('user is not exists,please re-enter')




if __name__ == '__main__':
    l=login('zxafy','123456')
    print(l.login_func())