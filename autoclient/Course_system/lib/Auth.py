#!/usr/bin/env python
#coding:utf-8
from Course_system.lib import Login
def auth(func):
    def wrapper(*args,**kwargs):
        while True:
            username = input('please input you username:').strip()
            password = input('please input you password:').strip()
            res_login = Login.login(username, password)
            res_data=res_login.login_func()
            if res_data:
                res=func(res_data)
                return res
            else:
                choise=input('Do you want to continue login?(y/n)').strip()
                if choise !='n':
                    continue
                else:
                    break

    return wrapper