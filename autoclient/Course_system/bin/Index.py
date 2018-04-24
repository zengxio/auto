#!/usr/bin/env python
#coding:utf-8
import sys
import os

from Course_system.lib import Login
from Course_system.lib import Open_file
from Course_system.src import Admin_class
from Course_system.src import Course_class
from Course_system.src import Student_class
from Course_system.src import Teacher_class
from Course_system.lib import Auth

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

print('Welcome to the course selection system'.center(60,"*"))
'''interface program'''

class interface_class:

    @Auth.auth
    def interface_program(res_data):
        pass



if __name__ == '__main__':
    interface_class.interface_program()
